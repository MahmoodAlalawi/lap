class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):

        self.__channel=Television.MIN_CHANNEL
        self.__volume=Television.MIN_VOLUME
        self.__TV_status= False



    def power(self):
        if not self.__TV_status:
             self.__TV_status=True
        elif self.__TV_status:
             self.__TV_status=False




    def channel_up(self):
        if self.__TV_status:
            if self.__channel==Television.MAX_CHANNEL:
                self.__channel=Television.MIN_CHANNEL
            else:
                self.__channel+=1



    def channel_down(self):
        if self.__TV_status:
            if self.__channel==Television.MIN_CHANNEL:
                self.__channel=Television.MAX_CHANNEL
            else:
                self.__channel-=1




    def volume_up(self):
        if self.__TV_status:
                if self.__volume<Television.MAX_VOLUME:
                       self.__volume+=1



    def volume_down(self):
        if self.__TV_status:
            if self.__volume > Television.MIN_VOLUME:
                 self.__volume-=1
        


    def __str__(self):
        return f"TV status: Is on ={self.__TV_status}, Channel = {self.__channel}, Volume = {self.__volume}"

