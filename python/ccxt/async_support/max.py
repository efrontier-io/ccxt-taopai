# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.async_support.base.exchange import Exchange

# -----------------------------------------------------------------------------

try:
    basestring  # Python 3
except NameError:
    basestring = str  # Python 2
import base64
import math
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import ArgumentsRequired
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidAddress
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import OrderNotFound


class max(Exchange):

    def describe(self):
        return self.deep_extend(super(max, self).describe(), {
            'id': 'max',
            'name': 'Max',
            'countries': ['TW'],
            'version': 'v2',
            'enableRateLimit': False,
            'rateLimit': 1200,
            'certified': False,
            'has': {
                'cancelAllOrders': True,
                'cancelOrder': True,
                'cancelOrders': False,
                'CORS': True,
                'createDepositAddress': True,
                'createLimitOrder': True,
                'createMarketOrder': True,
                'createOrder': True,
                'deposit': False,
                'editOrder': 'emulated',
                'fetchBalance': True,
                'fetchBidsAsks': False,
                'fetchClosedOrders': True,
                'fetchCurrencies': True,
                'fetchDepositAddress': True,
                'fetchDeposits': False,
                'fetchFundingFees': False,
                'fetchL2OrderBook': False,
                'fetchLedger': False,
                'fetchMarkets': True,
                'fetchMyTrades': True,
                'fetchOHLCV': True,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchOrderBook': True,
                'fetchOrderBooks': False,
                'fetchOrders': True,
                'fetchStatus': 'emulated',
                'fetchTicker': True,
                'fetchTickers': True,
                'fetchTime': True,
                'fetchTrades': True,
                'fetchTradingFee': False,
                'fetchTradingFees': False,
                'fetchTradingLimits': False,
                'fetchTransactions': False,
                'fetchWithdrawals': True,
                'privateAPI': True,
                'publicAPI': True,
                'withdraw': False,
            },
            'urls': {
                'logo': '',
                'api': {
                    'web': 'https://max.maicoin.com',
                    'wapi': '',
                    'public': 'https://max-api.maicoin.com',
                    'private': 'https://max-api.maicoin.com',
                },
                'www': 'https://max.maicoin.com',
                'doc': 'https://max.maicoin.com/documents/api',
                'fees': 'https://max.maicoin.com/docs/fees',
            },
            'api': {
                'web': {
                },
                'wapi': {
                },
                'public': {
                    'get': [
                        'markets',
                        'currencies',
                        'tickers/{market_id}',
                        'tickers',
                        'withdrawal/constraint',
                        'depth',
                        'trades',
                        'k',
                        'timestamp',
                    ],
                },
                'private': {
                    'get': [
                        'members/profile',
                        'members/accounts/{currency_id}',
                        'members/accounts',
                        'members/me',
                        'deposits',
                        'deposit',
                        'deposit_addresses',
                        'withdrawals',
                        'withdrawal',
                        'withdrawal_addresses',
                        'orders',
                        'order',
                        'trades/my/of_order',
                        'trades/my',
                        'internal_transfers',
                        'internal_transfer',
                        'rewards/{reward_type}',
                        'rewards',
                        'max_rewards/yesterday',
                    ],
                    'post': [
                        'deposit_addresses',
                        'orders/clear',
                        'orders',
                        'orders/multi',
                        'order/delete',
                    ],
                },
            },
            'timeframes': {
                '1m': '1',
                '5m': '5',
                '15m': '15',
                '30m': '30',
                '1h': '60',
                '2h': '120',
                '4h': '240',
                '6h': '360',
                '12h': '720',
                '1d': '1440',
                '3d': '4320',
                '1w': '10080',
            },
            'fees': {
                'trading': {
                    'maker': 0.05 / 100,
                    'taker': 0.15 / 100,
                },
                'funding': {
                    'withdraw': {},
                    'deposit': {},
                },
            },
            'commonCurrencies': {
            },
            'options': {
                'timeDifference': 0,  # the difference between system clock and Max clock
                'adjustForTimeDifference': False,  # controls the adjustment logic upon instantiation
            },
            'exceptions': {
                '2002': InvalidOrder,  # Order volume too small
                '2003': OrderNotFound,  # Failed to cancel order
                '2004': OrderNotFound,  # Order doesn't exist
                '2005': AuthenticationError,  # Signature is incorrect.
                '2006': AuthenticationError,  # The nonce has already been used by access key.
                '2007': AuthenticationError,  # The nonce is invalid.(30 secconds difference from server time)
                '2008': AuthenticationError,  # The access key does not exist.
                '2009': AuthenticationError,  # The access key is disabled.
                '2011': AuthenticationError,  # Requested API is out of access key scopes.
                '2014': AuthenticationError,  # Payload is not consistent with body or wrong path in payload.
                '2015': AuthenticationError,  # Payload is invalid
                '2016': InvalidOrder,  # amount_too_small
                '2018': InsufficientFunds,  # cannot lock funds
            },
        })

    async def fetch_time(self, params={}):
        response = await self.publicGetTimestamp()
        return int(response, 10) * 1000

    def nonce(self):
        return self.milliseconds() - self.options['timeDifference']

    async def load_time_difference(self):
        serverTimestamp = await self.fetch_time()
        after = self.milliseconds()
        self.options['timeDifference'] = after - serverTimestamp
        return self.options['timeDifference']

    def insert_objects_property_by(self, a, keyA, b, keyB, insertKey):
        result = {}
        for i in range(0, len(a)):
            entry = a[i]
            index = entry[keyA]
            result[index] = entry
        for i in range(0, len(b)):
            entry = b[i]
            index = entry[keyB]
            if result[index]:
                result[index][insertKey] = entry
        values = []
        resultKeys = list(result.keys())
        for i in range(0, len(resultKeys)):
            values.append(result[resultKeys[i]])
        return values

    async def fetch_currencies(self, params={}):
        currenciesResponse = await self.publicGetCurrencies(params)
        withdrawalResponse = await self.publicGetWithdrawalConstraint()
        response = self.insert_objects_property_by(
            currenciesResponse,
            'id',
            withdrawalResponse,
            'currency',
            'withdrawal'
        )
        result = {}
        for i in range(0, len(response)):
            currency = response[i]
            id = currency['id']
            code = self.safe_currency_code(id)
            fiat = id is True if 'twd' else False
            withdrawal = self.safe_value(currency, 'withdrawal')
            withdrawalFee = self.safe_value(withdrawal, 'fee')
            withdrawalLimit = self.safe_value(withdrawal, 'min_amount')
            result[code] = {
                'id': id,
                'code': code,
                'name': code,
                'active': True,
                'fiat': fiat,
                'precision': self.safe_integer(currency, 'precision'),
                'limits': {
                    'amount': {
                        'min': None,
                        'max': None,
                    },
                    'price': {
                        'min': None,
                        'max': None,
                    },
                    'deposit': {
                        'min': None,
                        'max': None,
                    },
                    'withdraw': {
                        'min': withdrawalLimit,
                        'max': None,
                    },
                },
                'funding': {
                    'withdraw': {
                        'fee': withdrawalFee,
                    },
                    'deposit': {
                        'fee': None,
                    },
                },
                'info': currency,
            }
        return result

    async def fetch_markets(self, params={}):
        markets = await self.publicGetMarkets()
        if self.options['adjustForTimeDifference']:
            await self.load_time_difference()
        result = []
        for i in range(0, len(markets)):
            market = markets[i]
            id = market['id']
            baseId = market['base_unit']
            quoteId = market['quote_unit']
            base = self.safe_currency_code(baseId)
            quote = self.safe_currency_code(quoteId)
            symbol = base + '/' + quote
            precision = {
                'amount': market['base_unit_precision'],
                'price': market['quote_unit_precision'],
            }
            active = True
            entry = {
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'info': market,
                'active': active,
                'precision': precision,
                'limits': {
                    'amount': {
                        'min': None,
                        'max': None,
                    },
                    'price': {
                        'min': None,
                        'max': None,
                    },
                    'cost': {
                        'min': None,
                        'max': None,
                    },
                },
            }
            result.append(entry)
        return result

    async def fetch_balance(self, params={}):
        await self.load_markets()
        response = await self.privateGetMembersAccounts(params)
        result = {'info': response}
        for i in range(0, len(response)):
            balance = response[i]
            currency = balance['currency']
            if currency in self.currencies_by_id:
                currency = self.currencies_by_id[currency]['code']
            account = self.account()
            account['free'] = self.safe_float(balance, 'balance')
            account['used'] = self.safe_float(balance, 'locked')
            account['total'] = self.sum(account['free'], account['used'])
            result[currency] = account
        return self.parse_balance(result)

    async def fetch_order_book(self, symbol, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'market': market['id'],
        }
        if limit is not None:
            request['limit'] = limit  # default = 300
        response = await self.publicGetDepth(self.extend(request, params))
        timestamp = self.safe_timestamp(response, 'timestamp')
        orderbook = self.parse_order_book(response, timestamp)
        return orderbook

    def parse_ticker(self, ticker, market=None):
        timestamp = self.safe_timestamp(ticker, 'at')
        symbol = None
        marketId = self.safe_string(ticker, 'symbol')
        if marketId in self.markets_by_id:
            market = self.markets_by_id[marketId]
        if market is not None:
            symbol = market['symbol']
        last = self.safe_float(ticker, 'last')
        open = self.safe_float(ticker, 'open')
        change = last - open
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_float(ticker, 'high'),
            'low': self.safe_float(ticker, 'low'),
            'bid': self.safe_float(ticker, 'buy'),
            'bidVolume': None,
            'ask': self.safe_float(ticker, 'sell'),
            'askVolume': None,
            'vwap': None,
            'open': open,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': change,
            'percentage': (change / open) * 100,
            'average': None,
            'baseVolume': self.safe_float(ticker, 'vol'),
            'quoteVolume': None,
            'info': ticker,
        }

    async def fetch_ticker(self, symbol, params={}):
        await self.load_markets()
        market = self.market(symbol)
        response = await self.publicGetTickersMarketId(self.extend({
            'market_id': market['id'],
        }, params))
        response['symbol'] = market['id']
        return self.parse_ticker(response, market)

    async def fetch_tickers(self, symbols=None, params={}):
        await self.load_markets()
        response = await self.publicGetTickers(params)
        tickerKeys = list(response.keys())
        result = {}
        for i in range(0, len(tickerKeys)):
            key = tickerKeys[i]
            response[key]['symbol'] = key
            ticker = self.parse_ticker(response[key])
            if symbols is None or symbols.includes(ticker['symbol']):
                result[ticker['symbol']] = ticker
        return result

    def parse_ohlcv(self, ohlcv, market=None, timeframe='1m', since=None, limit=None):
        return [
            int(ohlcv[0]) * 1000,
            float(ohlcv[1]),
            float(ohlcv[2]),
            float(ohlcv[3]),
            float(ohlcv[4]),
            float(ohlcv[5]),
        ]

    async def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'market': market['id'],
            'period': self.timeframes[timeframe],
        }
        if since is not None:
            request['timestamp'] = int(since) / 1000
        if limit is not None:
            request['limit'] = limit  # default = 30
        response = await self.publicGetK(self.extend(request, params))
        return self.parse_ohlcvs(response, market, timeframe, since, limit)

    def parse_deposit_address(self, code, response):
        if len(response) < 1:
            raise InvalidAddress(self.id + ' fetchDepositAddress ' + code + ' returned empty address.')
        depositAddress = response[0]
        address = self.safe_string(depositAddress, 'address')
        if address == 'suspended':
            raise InvalidAddress(self.id + ' fetchDepositAddress ' + code + ' returned an suspended address.')
        tag = None
        if code == 'XRP' and address:
            splitted = address.split('?dt=')
            address = splitted[0]
            tag = splitted[1]
        self.check_address(address)
        return {
            'info': response,
            'currency': code,
            'address': address,
            'tag': tag,
        }

    async def create_deposit_address(self, code, params={}):
        await self.load_markets()
        currency = self.currency(code)
        request = {
            'currency': currency['id'],
        }
        response = await self.privatePostDepositAddresses(self.extend(request, params))
        return self.parse_deposit_address(code, response)

    async def fetch_deposit_address(self, code, params={}):
        await self.load_markets()
        currency = self.currency(code)
        request = {
            'currency': currency['id'],
        }
        response = await self.privateGetDepositAddresses(self.extend(request, params))
        return self.parse_deposit_address(code, response)

    def parse_transaction_status_by_type(self, status, type=None):
        if type is None:
            return status
        statuses = {
            'deposit': {
                'submitting': 'pending',
                'cancelled': 'canceled',
                'submitted': 'pending',
                'suspended': 'pending',
                'rejected': 'failed',
                'accepted': 'ok',
                'refunded': 'failed',
                'suspect': 'pending',
                'refund_cancelled': 'ok',
            },
            'withdrawal': {
                'submitting': 'pending',
                'submitted': 'pending',
                'rejected': 'failed',
                'accepted': 'pending',
                'suspect': 'pending',
                'approved': 'pending',
                'processing': 'pending',
                'retryable': 'pending',
                'sent': 'pending',
                'canceled': 'canceled',
                'failed': 'failed',
                'pending': 'pending',
                'confirmed': 'ok',
                'kgi_manually_processing': 'pending',
                'kgi_instruction_sent': 'pending',
                'kgi_manually_confirmed': 'ok',
                'kgi_possible_failed': 'pending',
            },
        }
        return statuses[type][status] if (status in statuses[type]) else status

    def parse_transaction(self, transaction, currency=None):
        id = self.safe_string(transaction, 'uuid')
        txid = self.safe_string(transaction, 'txid')
        currencyId = self.safe_string(transaction, 'currency')
        code = self.safe_currency_code(currencyId, currency)
        timestamp = self.safe_timestamp(transaction, 'created_at')
        updated = self.safe_timestamp(transaction, 'updated_at')
        amount = self.safe_float(transaction, 'amount')
        feeCurrencyId = self.safe_string(transaction, 'fee_currency')
        feeCurrency = None
        if feeCurrencyId in self.currencies_by_id:
            feeCurrency = self.currencies_by_id[feeCurrencyId]
        if feeCurrency is not None:
            feeCurrencyId = feeCurrency['code']
        else:
            feeCurrencyId = self.safe_currency_code(feeCurrencyId)
        fee = {
            'cost': self.safe_float(transaction, 'fee'),
            'currency': feeCurrencyId,
        }
        type = self.safe_string(transaction, 'type')
        status = self.parse_transaction_status_by_type(self.safe_string(transaction, 'state'), type)
        return {
            'info': transaction,
            'id': id,
            'txid': txid,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'address': None,
            'tag': None,
            'type': type,
            'amount': amount,
            'currency': code,
            'status': status,
            'updated': updated,
            'fee': fee,
        }

    async def fetch_withdrawals(self, code=None, since=None, limit=None, params={}):
        await self.load_markets()
        currency = None
        request = {}
        if code is not None:
            currency = self.currency(code)
            request['currency'] = currency['id']
        if since is not None:
            request['from'] = int(math.floor(int(since, 10)) / 1000)
        if limit is not None:
            request['limit'] = limit
        response = await self.privateGetWithdrawals(self.extend(request, params))
        for i in range(0, len(response)):
            response[i]['type'] = 'withdrawal'
        return self.parse_transactions(response, currency, since, limit)

    async def fetch_deposits(self, code=None, since=None, limit=None, params={}):
        await self.load_markets()
        currency = None
        request = {}
        if code is not None:
            currency = self.currency(code)
            request['currency'] = currency['id']
        if since is not None:
            request['from'] = int(math.floor(int(since, 10)) / 1000)
        if limit is not None:
            request['limit'] = limit
        response = await self.privateGetDeposits(self.extend(request, params))
        for i in range(0, len(response)):
            response[i]['type'] = 'deposit'
        return self.parse_transactions(response, currency, since, limit)

    def parse_trade(self, trade, market=None):
        #
        # public trades
        #
        #    {
        #        "id": 4813073,
        #        "price": "3980.0",
        #        "volume": "0.000264",
        #        "funds": "1.05072",
        #        "market": "btcusdt",
        #        "market_name": "BTC/USDT",
        #        "created_at": 1553341297,
        #        "side": "bid"
        #    }
        #
        #
        # private trades
        #
        #    {
        #        "id": 3175037,
        #        "price": "3986.97",
        #        "volume": "0.125",
        #        "funds": "498.37125",
        #        "market": "btcusdt",
        #        "market_name": "BTC/USDT",
        #        "created_at": 1543941724,
        #        "side": "ask",
        #        "fee": "0.747557",
        #        "fee_currency": "usdt",
        #        "order_id": 18298466
        #        "info": {
        #            "maker": "ask",
        #            "ask": {"fee": "0.747557", "fee_currency": "usdt", "order_id": 18298466},
        #            "bid": null
        #        }
        #    }
        timestamp = self.safe_timestamp(trade, 'created_at')
        price = self.safe_float(trade, 'price')
        amount = self.safe_float(trade, 'volume')
        id = self.safe_string(trade, 'id')
        side = self.safe_string(trade, 'side')
        order = self.safe_string(trade, 'order_id')
        cost = self.safe_float(trade, 'funds')
        fee = None
        if 'fee' in trade:
            fee = {
                'cost': self.safe_float(trade, 'fee'),
                'currency': self.safe_currency_code(trade['fee_currency']),
            }
        tradeInfo = self.safe_value(trade, 'info')
        tradeMakerSide = self.safe_string_2(tradeInfo, 'maker')
        takerOrMaker = None
        if tradeMakerSide is not None and side is not None:
            takerOrMaker = 'maker' if (tradeMakerSide == side) else 'taker'
        symbol = None
        if market is None:
            marketId = self.safe_string(trade, 'market')
            market = self.safe_value(self.markets_by_id, marketId)
        if market is not None:
            symbol = market['symbol']
        return {
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'id': id,
            'order': order,
            'type': None,
            'takerOrMaker': takerOrMaker,
            'side': side,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': fee,
        }

    async def fetch_trades(self, symbol, since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'market': market['id'],
        }
        # since is not supported
        # if since is not None:
        #     request['timestamp'] = int(math.floor(int(since, 10)) / 1000)
        # }
        if limit is not None:
            request['limit'] = limit  # default = 50, maximum = 1000
        response = await self.publicGetTrades(self.extend(request, params))
        return self.parse_trades(response, market, since, limit)

    async def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        if symbol is None:
            raise ArgumentsRequired(self.id + ' fetchMyTrades requires a symbol argument')
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'market': market['id'],
        }
        if limit is not None:
            request['limit'] = limit
        # since is not supported
        # if since is not None:
        #     request['timestamp'] = int(math.floor(int(since, 10)) / 1000)
        # }
        response = await self.privateGetTradesMy(self.extend(request, params))
        return self.parse_trades(response, market, since, limit)

    def parse_order_status(self, status):
        statuses = {
            'wait': 'open',
            'cancel': 'canceled',
            'done': 'closed',
            'convert': 'open',
            'finalizing': 'open',
            'failed': 'canceled',
        }
        return statuses[status] if (status in statuses) else status

    def parse_order(self, order, market=None):
        status = self.parse_order_status(self.safe_string(order, 'state'))
        symbol = None
        marketId = self.safe_string(order, 'market')
        if marketId in self.markets_by_id:
            market = self.markets_by_id[marketId]
        if market is not None:
            symbol = market['symbol']
        timestamp = self.safe_timestamp(order, 'created_at')
        id = self.safe_string(order, 'id')
        price = self.safe_float(order, 'price')
        amount = self.safe_float(order, 'volume')
        average = self.safe_float(order, 'avg_price')
        filled = self.safe_float(order, 'executed_volume')
        cost = None
        remaining = self.safe_float(order, 'remaining_volume')
        type = self.safe_string(order, 'ord_type')
        if type is not None:
            if type == 'market':
                if price is None:
                    price = average
        if price is not None:
            cost = price * filled
        side = self.safe_string(order, 'side')
        result = {
            'info': order,
            'id': id,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'symbol': symbol,
            'type': type,
            'side': side,
            'price': price,
            'amount': amount,
            'cost': cost,
            'average': average,
            'filled': filled,
            'remaining': remaining,
            'status': status,
            'fee': None,
            'trades': None,
        }
        return result

    async def create_order(self, symbol, type, side, amount, price=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        lowercaseType = type.lower()
        order = {
            'market': market['id'],
            'volume': self.amount_to_precision(symbol, amount),
            'ord_type': lowercaseType,
            'side': side,
        }
        priceIsRequired = False
        stopPriceIsRequired = False
        if lowercaseType == 'limit' or lowercaseType == 'stop_limit':
            priceIsRequired = True
        if lowercaseType == 'stop_limit' or lowercaseType == 'stop_market':
            stopPriceIsRequired = True
        if priceIsRequired:
            if price is None:
                raise InvalidOrder(self.id + ' createOrder method requires a price argument for a ' + lowercaseType + ' order')
            order['price'] = self.price_to_precision(symbol, price)
        if stopPriceIsRequired:
            stop_price = self.safe_float(params, 'stop_price')
            if stop_price is None:
                raise InvalidOrder(self.id + ' createOrder method requires a stop_price extra param for a ' + lowercaseType + ' order')
            params = self.omit(params, 'stop_price')
            order['stop_price'] = self.price_to_precision(symbol, stop_price)
        response = await self.privatePostOrders(self.extend(order, params))
        return self.parse_order(response, market)

    async def cancel_all_orders(self, symbol=None, params={}):
        request = {}
        if symbol is not None:
            await self.load_markets()
            market = self.market(symbol)
            request['market'] = market['id']
        return self.privatePostOrdersClear(self.extend(request, params))

    async def cancel_order(self, id, symbol=None, params={}):
        request = {
            'id': id,
        }
        response = await self.privatePostOrderDelete(self.extend(request, params))
        return self.parse_order(response)

    async def fetch_order(self, id, symbol=None, params={}):
        if id is None:
            raise ArgumentsRequired(self.id + ' fetchOrder requires a id argument')
        await self.load_markets()
        request = {
            'id': id,
        }
        response = await self.privateGetOrder(request)
        return self.parse_order(response)

    async def fetch_orders(self, symbol=None, since=None, limit=None, params={}):
        if symbol is None:
            raise ArgumentsRequired(self.id + ' fetchOrders requires a symbol argument')
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'market': market['id'],
        }
        if limit is not None:
            request['limit'] = limit
        # since is not supported
        # if since is not None:
        #     request['timestamp'] = int(math.floor(int(since, 10)) / 1000)
        # }
        response = await self.privateGetOrders(self.extend(request, params))
        return self.parse_orders(response, market, since, limit)

    async def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        return self.fetch_orders(symbol, since, limit, self.extend(params, {'state': ['cancel', 'done', 'failed']}))

    async def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        return self.fetch_orders(symbol, since, limit, self.extend(params, {'state': ['wait', 'convert', 'finalizing']}))

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        newParams = params
        request = '/api/' + self.version + '/' + self.implode_params(path, params)
        url = self.urls['api'][api]
        url += request
        if not headers:
            headers = {}
        headers['X-MAX-AGENT'] = 'ccxt'
        if api == 'private':
            self.check_required_credentials()
            newParams = self.extend(params, {
                'nonce': self.nonce(),
                'path': request,
            })
            payload = base64.b64encode(self.encode(self.json(newParams)))
            signature = self.hmac(payload, self.encode(self.secret))
            headers = self.extend(headers, {
                'X-MAX-ACCESSKEY': self.apiKey,
                'X-MAX-PAYLOAD': self.decode(payload),
                'X-MAX-SIGNATURE': signature,
            })
        if method == 'GET' or method == 'DELETE':
            if not self.is_empty(newParams):
                newParamsIsArray = {}
                newParamsOthers = {}
                newParamsKeys = list(newParams.keys())
                for i in range(0, len(newParamsKeys)):
                    key = newParamsKeys[i]
                    if isinstance(newParams[key], list):
                        newParamsIsArray[key] = newParams[key]
                    else:
                        newParamsOthers[key] = newParams[key]
                url += '?'
                if not self.is_empty(newParamsOthers):
                    url += self.urlencode(newParamsOthers)
                if not self.is_empty(newParamsOthers) and not self.is_empty(newParamsIsArray):
                    url += '&'
                if not self.is_empty(newParamsIsArray):
                    result = []
                    newParamsIsArrayKeys = list(newParamsIsArray.keys())
                    for i in range(0, len(newParamsIsArrayKeys)):
                        key = newParamsIsArrayKeys[i]
                        for j in range(0, len(newParamsIsArray[key])):
                            result.append(key + '%5B%5D=' + newParamsIsArray[key][j])
                    url += '&'.join(result)
        else:
            body = self.json(newParams)
            headers = self.extend(headers, {
                'Content-Type': 'application/json',
            })
        return {
            'url': url,
            'method': method,
            'body': body,
            'headers': headers,
        }

    def handle_errors(self, httpCode, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if response is None:
            return  # fallback to default error handler
        error = self.safe_value(response, 'error')
        if isinstance(error, basestring):
            return
        code = error and self.safe_string(error, 'code')
        if code:
            feedback = self.id + ' ' + self.safe_string(error, 'message')
            if code in self.exceptions:
                raise self.exceptions[code](feedback)
            else:
                raise ExchangeError(feedback)
