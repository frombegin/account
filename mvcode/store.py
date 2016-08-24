DEFAULT_MVCODE_EXPIRATION_TIME = 30  # 30 seconds


class Store:
    def save(self, mobile, used_for, mvcode):
        """

        :param mobile:
        :param used_for:
        :param mvcode:
        :return:
        """

    def verify(self, mobile, used_for, mvcode):
        """
        检验 mvcode
        :param mobile:
        :param used_for:
        :param mvcode:
        :return:
        """
        return True

    def _create_key(self, mobile, used_for):
        return "{}-{}".format(mobile, used_for)


class RedisStore(Store):
    def save(self, mobile, used_for, mvcode):
        pass

    def verify(self, mobile, used_for, mvcode):
        pass
