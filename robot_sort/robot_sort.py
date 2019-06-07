class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def move_up_list(self):
        while self.can_move_right():
            # Drop Current Item. Grab item in front of us.
            self.swap_item()
            self.move_right()
            if self.compare_item() == 1:
                # Item holding was greater. Need to swap with current item and to left.
                self.swap_item()
                self.move_left()
                self.swap_item()
                self.move_right()
                # Swap -> Take new item left -> swap -> take item right
                # Turn light on to indicate we swapped
                self.set_light_on()
            else:
                # Current item is either less than or equal to item in front of us.
                # Put the lesser item to the left and take the new item.
                self.move_left()
                self.swap_item()
                self.move_right()

    def move_down_list(self):
        while self.can_move_left():
            # Drop Current Item. Grab item in front of us.
            self.swap_item()
            self.move_left()
            if self.compare_item() == -1:
                # Item holding was less. Need to swap with current item and to right.
                self.swap_item()
                self.move_right()
                self.swap_item()
                self.move_left()
                self.set_light_on()
            else:
                self.move_right()
                self.swap_item()
                self.move_left()

    def sort_initial(self):
        # Runtime on this is horrendous. Fails first time test. Attempting stretch.
        while self.can_move_right():
            # On final position, can move right will change after we move up list for last step.
            # Once that happens, run can move right again, and put a loop inside to go left.
            self.move_up_list()
            if not self.can_move_right():
                # This means we reached end of list. We need to make sure to turn the light off so that no swaps are present.
                self.set_light_off()
                self.move_down_list()

                # If light is on, there is still some swapping happening. Loop again.
                if self.light_is_on():
                    self.set_light_off()
                # Otherwise, return from loop.
                else:
                    return

    def sort(self):
        # Need to improve timing, making too many passes.
        # Selection sort concept. One wrapper loop with two inner loops.
        while self.can_move_right():
            self.swap_item()
            while self.can_move_right():
                self.move_right()

                if self.compare_item() == 1:
                    self.swap_item()

            while self.compare_item() != None:
                self.move_left()

            self.swap_item()
            self.move_right()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
