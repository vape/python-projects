from Classes.utils import initializer
from uuid import uuid4
from datetime import datetime


class VideoAlreadyCheckedOutException(BaseException):
    @initializer
    def __init__(self, video):
        pass


class Customer(object):
    @initializer(private=True)
    def __init__(self, name):
        self._uid = uuid4()

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name


class Video(object):
    @initializer(private=True)
    def __init__(self, video_id, title):
        self._checkout_date = None
        self._expected_return_date = None

    @property
    def video_id(self):
        return self._video_id

    @property
    def title(self):
        return self._title

    @property
    def checkout_date(self):
        return self._checkout_date

    @property
    def expected_return_date(self):
        return self._expected_return_date

    @property
    def is_checked_out(self):
        return self._checkout_date and self._expected_return_date

    def check_out(self, co_date, exp_ret_date):
        if self.is_checked_out:
            raise VideoAlreadyCheckedOutException(self)
        if not isinstance(co_date, datetime) or not isinstance(exp_ret_date, datetime):
            raise ValueError('co_date and exp_ret_date should have type datetime')
        if exp_ret_date <= co_date:
            raise ValueError('exp_ret_date must be greater than co_date')

        self._checkout_date = co_date
        self._expected_return_date = exp_ret_date

    def return_video(self):
        self._checkout_date = None
        self._expected_return_date = None


class Transaction(object):
    @initializer(private=True)
    def __init__(self, customer_id, video_id, checkout_date, expected_return_date):
        pass

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def video_id(self):
        return self._video_id

    @property
    def checkout_date(self):
        return self._checkout_date

    @property
    def expected_return_date(self):
        return self._expected_return_date


class MovieStore(object):
    def __init__(self):
        self._customers = dict()
        self._videos = dict()
        self._transactions = []

    def add_customer(self, name):
        cust = Customer(name)
        self._customers[cust.uid] = cust
        return cust

    def get_customer(self, uid):
        return self._customers.get(uid)

    def find_customer(self, name):
        return [c for c in self._customers.values() if name.lower() in c.name.lower()]

    def add_video(self, video):
        self._videos[video.video_id] = video

    def get_video(self, video_id):
        return self._videos.get(video_id)

    def checkout_video(self, video_id, customer, expected_return_date):
        customer = customer.uid if isinstance(customer, Customer) else customer
        cust = self.get_customer(customer)
        if not cust:
            raise ValueError('Customer with id {0} does not exist.'.format(customer))

        vid = self.get_video(video_id)
        if not vid:
            raise ValueError('Video with id {0} does not exist.'.format(video_id))

        if vid.is_checked_out:
            raise ValueError('Video with id {0} is already checked out. Expected return date is: {1}'.format(video_id,
                                                                                                             vid.expected_return_date))

        now = datetime.now()
        if expected_return_date <= now:
            raise ValueError('expected_return_date cannot be smaller than current time.')

        vid.check_out(now, expected_return_date)
        trx = Transaction(customer, vid.video_id, now, expected_return_date)
        self._transactions.append(trx)
        return trx

    def _calculate_late_return_fee(self, video, actual_ret_date):
        return 5


    def return_video(self, video_id, return_date):
        vid = self.get_video(video_id)
        if not vid.is_checked_out:
            raise ValueError('Video with id {0} is not checked out.'.format(video_id))

        late_return_fee = 0 if return_date <= vid.expected_return_date else self._calculate_late_return_fee(vid,
                                                                                                            return_date)

        vid.return_video()
        return late_return_fee





