# coding: utf-8

"""
    Gate API v4

    APIv4 futures provides all sorts of futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    OpenAPI spec version: 1.2.1
    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Position(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'user': 'int',
        'contract': 'str',
        'size': 'int',
        'leverage': 'str',
        'risk_limit': 'str',
        'leverage_max': 'str',
        'maintenance_rate': 'str',
        'value': 'str',
        'margin': 'str',
        'entry_price': 'str',
        'liq_price': 'str',
        'mark_price': 'str',
        'unrealised_pnl': 'str',
        'realised_pnl': 'str',
        'history_pnl': 'str',
        'last_close_pnl': 'str',
        'adl_ranking': 'int',
        'pending_orders': 'int',
        'close_order': 'PositionCloseOrder'
    }

    attribute_map = {
        'user': 'user',
        'contract': 'contract',
        'size': 'size',
        'leverage': 'leverage',
        'risk_limit': 'risk_limit',
        'leverage_max': 'leverage_max',
        'maintenance_rate': 'maintenance_rate',
        'value': 'value',
        'margin': 'margin',
        'entry_price': 'entry_price',
        'liq_price': 'liq_price',
        'mark_price': 'mark_price',
        'unrealised_pnl': 'unrealised_pnl',
        'realised_pnl': 'realised_pnl',
        'history_pnl': 'history_pnl',
        'last_close_pnl': 'last_close_pnl',
        'adl_ranking': 'adl_ranking',
        'pending_orders': 'pending_orders',
        'close_order': 'close_order'
    }

    def __init__(self, user=None, contract=None, size=None, leverage=None, risk_limit=None, leverage_max=None, maintenance_rate=None, value=None, margin=None, entry_price=None, liq_price=None, mark_price=None, unrealised_pnl=None, realised_pnl=None, history_pnl=None, last_close_pnl=None, adl_ranking=None, pending_orders=None, close_order=None):  # noqa: E501
        """Position - a model defined in OpenAPI"""  # noqa: E501

        self._user = None
        self._contract = None
        self._size = None
        self._leverage = None
        self._risk_limit = None
        self._leverage_max = None
        self._maintenance_rate = None
        self._value = None
        self._margin = None
        self._entry_price = None
        self._liq_price = None
        self._mark_price = None
        self._unrealised_pnl = None
        self._realised_pnl = None
        self._history_pnl = None
        self._last_close_pnl = None
        self._adl_ranking = None
        self._pending_orders = None
        self._close_order = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if contract is not None:
            self.contract = contract
        if size is not None:
            self.size = size
        if leverage is not None:
            self.leverage = leverage
        if risk_limit is not None:
            self.risk_limit = risk_limit
        if leverage_max is not None:
            self.leverage_max = leverage_max
        if maintenance_rate is not None:
            self.maintenance_rate = maintenance_rate
        if value is not None:
            self.value = value
        if margin is not None:
            self.margin = margin
        if entry_price is not None:
            self.entry_price = entry_price
        if liq_price is not None:
            self.liq_price = liq_price
        if mark_price is not None:
            self.mark_price = mark_price
        if unrealised_pnl is not None:
            self.unrealised_pnl = unrealised_pnl
        if realised_pnl is not None:
            self.realised_pnl = realised_pnl
        if history_pnl is not None:
            self.history_pnl = history_pnl
        if last_close_pnl is not None:
            self.last_close_pnl = last_close_pnl
        if adl_ranking is not None:
            self.adl_ranking = adl_ranking
        if pending_orders is not None:
            self.pending_orders = pending_orders
        if close_order is not None:
            self.close_order = close_order

    @property
    def user(self):
        """Gets the user of this Position.  # noqa: E501

        User ID  # noqa: E501

        :return: The user of this Position.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Position.

        User ID  # noqa: E501

        :param user: The user of this Position.  # noqa: E501
        :type: int
        """

        self._user = user

    @property
    def contract(self):
        """Gets the contract of this Position.  # noqa: E501

        Futures contract  # noqa: E501

        :return: The contract of this Position.  # noqa: E501
        :rtype: str
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this Position.

        Futures contract  # noqa: E501

        :param contract: The contract of this Position.  # noqa: E501
        :type: str
        """

        self._contract = contract

    @property
    def size(self):
        """Gets the size of this Position.  # noqa: E501

        Position size  # noqa: E501

        :return: The size of this Position.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Position.

        Position size  # noqa: E501

        :param size: The size of this Position.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def leverage(self):
        """Gets the leverage of this Position.  # noqa: E501

        Position leverage  # noqa: E501

        :return: The leverage of this Position.  # noqa: E501
        :rtype: str
        """
        return self._leverage

    @leverage.setter
    def leverage(self, leverage):
        """Sets the leverage of this Position.

        Position leverage  # noqa: E501

        :param leverage: The leverage of this Position.  # noqa: E501
        :type: str
        """

        self._leverage = leverage

    @property
    def risk_limit(self):
        """Gets the risk_limit of this Position.  # noqa: E501

        Position risk limit  # noqa: E501

        :return: The risk_limit of this Position.  # noqa: E501
        :rtype: str
        """
        return self._risk_limit

    @risk_limit.setter
    def risk_limit(self, risk_limit):
        """Sets the risk_limit of this Position.

        Position risk limit  # noqa: E501

        :param risk_limit: The risk_limit of this Position.  # noqa: E501
        :type: str
        """

        self._risk_limit = risk_limit

    @property
    def leverage_max(self):
        """Gets the leverage_max of this Position.  # noqa: E501

        Maximum leverage under current risk limit  # noqa: E501

        :return: The leverage_max of this Position.  # noqa: E501
        :rtype: str
        """
        return self._leverage_max

    @leverage_max.setter
    def leverage_max(self, leverage_max):
        """Sets the leverage_max of this Position.

        Maximum leverage under current risk limit  # noqa: E501

        :param leverage_max: The leverage_max of this Position.  # noqa: E501
        :type: str
        """

        self._leverage_max = leverage_max

    @property
    def maintenance_rate(self):
        """Gets the maintenance_rate of this Position.  # noqa: E501

        Maintenance rate under current risk limit  # noqa: E501

        :return: The maintenance_rate of this Position.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_rate

    @maintenance_rate.setter
    def maintenance_rate(self, maintenance_rate):
        """Sets the maintenance_rate of this Position.

        Maintenance rate under current risk limit  # noqa: E501

        :param maintenance_rate: The maintenance_rate of this Position.  # noqa: E501
        :type: str
        """

        self._maintenance_rate = maintenance_rate

    @property
    def value(self):
        """Gets the value of this Position.  # noqa: E501

        Position value calculated in settlement currency  # noqa: E501

        :return: The value of this Position.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Position.

        Position value calculated in settlement currency  # noqa: E501

        :param value: The value of this Position.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def margin(self):
        """Gets the margin of this Position.  # noqa: E501

        Position margin  # noqa: E501

        :return: The margin of this Position.  # noqa: E501
        :rtype: str
        """
        return self._margin

    @margin.setter
    def margin(self, margin):
        """Sets the margin of this Position.

        Position margin  # noqa: E501

        :param margin: The margin of this Position.  # noqa: E501
        :type: str
        """

        self._margin = margin

    @property
    def entry_price(self):
        """Gets the entry_price of this Position.  # noqa: E501

        Entry price  # noqa: E501

        :return: The entry_price of this Position.  # noqa: E501
        :rtype: str
        """
        return self._entry_price

    @entry_price.setter
    def entry_price(self, entry_price):
        """Sets the entry_price of this Position.

        Entry price  # noqa: E501

        :param entry_price: The entry_price of this Position.  # noqa: E501
        :type: str
        """

        self._entry_price = entry_price

    @property
    def liq_price(self):
        """Gets the liq_price of this Position.  # noqa: E501

        Liquidation price  # noqa: E501

        :return: The liq_price of this Position.  # noqa: E501
        :rtype: str
        """
        return self._liq_price

    @liq_price.setter
    def liq_price(self, liq_price):
        """Sets the liq_price of this Position.

        Liquidation price  # noqa: E501

        :param liq_price: The liq_price of this Position.  # noqa: E501
        :type: str
        """

        self._liq_price = liq_price

    @property
    def mark_price(self):
        """Gets the mark_price of this Position.  # noqa: E501

        Current mark price  # noqa: E501

        :return: The mark_price of this Position.  # noqa: E501
        :rtype: str
        """
        return self._mark_price

    @mark_price.setter
    def mark_price(self, mark_price):
        """Sets the mark_price of this Position.

        Current mark price  # noqa: E501

        :param mark_price: The mark_price of this Position.  # noqa: E501
        :type: str
        """

        self._mark_price = mark_price

    @property
    def unrealised_pnl(self):
        """Gets the unrealised_pnl of this Position.  # noqa: E501

        Unrealized PNL  # noqa: E501

        :return: The unrealised_pnl of this Position.  # noqa: E501
        :rtype: str
        """
        return self._unrealised_pnl

    @unrealised_pnl.setter
    def unrealised_pnl(self, unrealised_pnl):
        """Sets the unrealised_pnl of this Position.

        Unrealized PNL  # noqa: E501

        :param unrealised_pnl: The unrealised_pnl of this Position.  # noqa: E501
        :type: str
        """

        self._unrealised_pnl = unrealised_pnl

    @property
    def realised_pnl(self):
        """Gets the realised_pnl of this Position.  # noqa: E501

        Realized PNL  # noqa: E501

        :return: The realised_pnl of this Position.  # noqa: E501
        :rtype: str
        """
        return self._realised_pnl

    @realised_pnl.setter
    def realised_pnl(self, realised_pnl):
        """Sets the realised_pnl of this Position.

        Realized PNL  # noqa: E501

        :param realised_pnl: The realised_pnl of this Position.  # noqa: E501
        :type: str
        """

        self._realised_pnl = realised_pnl

    @property
    def history_pnl(self):
        """Gets the history_pnl of this Position.  # noqa: E501

        History realized PNL  # noqa: E501

        :return: The history_pnl of this Position.  # noqa: E501
        :rtype: str
        """
        return self._history_pnl

    @history_pnl.setter
    def history_pnl(self, history_pnl):
        """Sets the history_pnl of this Position.

        History realized PNL  # noqa: E501

        :param history_pnl: The history_pnl of this Position.  # noqa: E501
        :type: str
        """

        self._history_pnl = history_pnl

    @property
    def last_close_pnl(self):
        """Gets the last_close_pnl of this Position.  # noqa: E501

        PNL of last position close  # noqa: E501

        :return: The last_close_pnl of this Position.  # noqa: E501
        :rtype: str
        """
        return self._last_close_pnl

    @last_close_pnl.setter
    def last_close_pnl(self, last_close_pnl):
        """Sets the last_close_pnl of this Position.

        PNL of last position close  # noqa: E501

        :param last_close_pnl: The last_close_pnl of this Position.  # noqa: E501
        :type: str
        """

        self._last_close_pnl = last_close_pnl

    @property
    def adl_ranking(self):
        """Gets the adl_ranking of this Position.  # noqa: E501

        ADL ranking, range from 1 to 5  # noqa: E501

        :return: The adl_ranking of this Position.  # noqa: E501
        :rtype: int
        """
        return self._adl_ranking

    @adl_ranking.setter
    def adl_ranking(self, adl_ranking):
        """Sets the adl_ranking of this Position.

        ADL ranking, range from 1 to 5  # noqa: E501

        :param adl_ranking: The adl_ranking of this Position.  # noqa: E501
        :type: int
        """

        self._adl_ranking = adl_ranking

    @property
    def pending_orders(self):
        """Gets the pending_orders of this Position.  # noqa: E501

        Current open orders  # noqa: E501

        :return: The pending_orders of this Position.  # noqa: E501
        :rtype: int
        """
        return self._pending_orders

    @pending_orders.setter
    def pending_orders(self, pending_orders):
        """Sets the pending_orders of this Position.

        Current open orders  # noqa: E501

        :param pending_orders: The pending_orders of this Position.  # noqa: E501
        :type: int
        """

        self._pending_orders = pending_orders

    @property
    def close_order(self):
        """Gets the close_order of this Position.  # noqa: E501


        :return: The close_order of this Position.  # noqa: E501
        :rtype: PositionCloseOrder
        """
        return self._close_order

    @close_order.setter
    def close_order(self, close_order):
        """Sets the close_order of this Position.


        :param close_order: The close_order of this Position.  # noqa: E501
        :type: PositionCloseOrder
        """

        self._close_order = close_order

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Position):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
