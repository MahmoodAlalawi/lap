class Television:
    """
    A class representing the Television Modifications
    """
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self):
        """
        Constructor to create initial sates for the TV
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__TV_status = False

    def power(self):
        """
        method that used to turn the TV on/off.

        :return: TV status
        """

        if not self.__TV_status:
            self.__TV_status = True
        elif self.__TV_status:
            self.__TV_status = False

    def channel_up(self):
        """
        This method  used to adjust the TV channel by incrementing its value

        :return: channel number
        """
        if self.__TV_status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """
        his method  used to adjust the TV channel by decrementing its value.

        :return:channel number
        """

        if self.__TV_status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """
        This method  used to adjust the TV volume by incrementing its value.
        :return:TV value
        """
        if self.__TV_status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        This method used to adjust the TV volume by decrementing its value.
        :return: TV value
        """
        if self.__TV_status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        This method should be used to return the TV status .
        :return: TV status
        """
        return f"TV status: Is on ={self.__TV_status}, Channel = {self.__channel}, Volume = {self.__volume}"