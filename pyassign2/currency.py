
"""Currency.py: Help to exchange the money you have into another currency.

__author__ = "Wangtie"
__pkuid__  = "1800011811"
__email__  = "1800011811@pku.edu.cn"
"""


short = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG',
         'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND',
         'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYR', 'BZD', 'CAD',
         'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP',
         'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EEK', 'EGP', 'ERN',
         'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP',
         'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF',
         'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD',
         'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD',
         'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL',
         'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO',
         'MTL', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN',
         'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP',
         'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR',
         'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD',
         'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP',
         'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS',
         'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR',
         'XOF', 'XPD', 'XPF', 'XPT', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL']

def test_from(a):
    '''straightforward way of testing whether from is valid'''
    global short
    if a in short:
        pass  #really straightforward
    else:
        print("Source currency code is invalid.")


def test_to(a):
    '''simple way if testing whether to is also valid'''
    global short
    if a in short:
        pass  #rather simple
    else:
        print("Exchange currency code is invalid.")


def exchange(currency_from, currency_to, amount_from):

    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""

    global short

    name = ['United Arab Emirates Dirham', 'Afghan Afghani', 'Albanian Lek',
            'Armenian Dram', 'Netherlands Antillean Guilder', 'Angolan Kwanza',
            'Argentine Peso', 'Australian Dollar', 'Aruban Florin',
            'Azerbaijani Manat', 'Bosnia-Herzegovina Convertible Mark',
            'Barbadian Dollar', 'Bangladeshi Taka', 'Bulgarian Lev',
            'Bahraini Dinar', 'Burundian Franc', 'Bermudan Dollar',
            'Brunei Dollar', 'Bolivian Boliviano', 'Brazilian Real',
            'Bahamian Dollar', 'Bitcoin', 'Bhutanese Ngultrum',
            'Botswanan Pula', 'Belarusian Ruble', 'Belize Dollar',
            'Canadian Dollar', 'Congolese Franc', 'Swiss Franc',
            'Chilean Unidad de Fomento', 'Chilean Peso', 'Chinese Yuan',
            'Colombian Peso', 'Costa Rican Colon', 'Cuban Convertible Peso',
            'Cuban Peso', 'Cape Verdean Escudo', 'Czech Republic Koruna',
            'Djiboutian Franc', 'Danish Krone', 'Dominican Peso',
            'Algerian Dinar', 'Estonian Kroon', 'Egyptian Pound',
            'Eritrean Nakfa', 'Ethiopian Birr', 'Euro', 'Fijian Dollar',
            'Falkland Islands Pound', 'British Pound Sterling',
            'Georgian Lari', 'Guernsey Pound', 'Ghanaian Cedi',
            'Gibraltar Pound', 'Gambian Dalasi', 'Guinean Franc',
            'Guatemalan Quetzal', 'Guyanaese Dollar', 'Hong Kong Dollar',
            'Honduran Lempira', 'Croatian Kuna', 'Haitian Gourde',
            'Hungarian Forint', 'Indonesian Rupiah', 'Israeli New Sheqel',
            'Manx pound', 'Indian Rupee', 'Iraqi Dinar', 'Iranian Rial',
            'Icelandic Kr\u00f3nur', 'Jersey Pound', 'Jamaican Dollar',
            'Jordanian Dinar', 'Japanese Yen', 'Kenyan Shilling',
            'Kyrgystani Som', 'Cambodian Riel', 'Comorian Franc',
            'North Korean Won', 'South Korean Won', 'Kuwaiti Dinar',
            'Cayman Islands Dollar', 'Kazakhstani Tenge', 'Laotian Kip',
            'Lebanese Pound', 'Sri Lankan Rupee', 'Liberian Dollar',
            'Lesotho Loti', 'Lithuanian Litas', 'Latvian Lats',
            'Libyan Dinar', 'Moroccan Dirham', 'Moldovan Leu',
            'Malagasy Ariary', 'Macedonian Denar', 'Myanma Kyat',
            'Mongolian Tugrik', 'Macanese Pataca', 'Mauritanian Ouguiya',
            'Maltese Lira', 'Mauritian Rupee', 'Maldivian Rufiyaa',
            'Malawian Kwacha', 'Mexican Peso', 'Malaysian Ringgit',
            'Mozambican Metical', 'Namibian Dollar', 'Nigerian Naira',
            'Nicaraguan Cordoba', 'Norwegian Krone', 'Nepalese Rupee',
            'New Zealand Dollar', 'Omani Rial', 'Panamanian Balboa',
            'Peruvian Nuevo Sol', 'Papua New Guinean Kina', 'Philippine Peso',
            'Pakistani Rupee', 'Polish Zloty', 'Paraguayan Guarani',
            'Qatari Rial', 'Romanian Leu', 'Serbian Dinar', 'Russian Ruble',
            'Rwandan Franc', 'Saudi Riyal', 'Solomon Islands Dollar',
            'Seychellois Rupee', 'Sudanese Pound', 'Swedish Krona',
            'Singapore Dollar', 'Saint Helena Pound', 'Sierra Leonean Leone',
            'Somali Shilling', 'Surinamese Dollar',
            'Sao Tome and Principe Dobra', 'Salvadoran Colon',
            'Syrian Pound', 'Swazi Lilangeni', 'Thai Baht',
            'Tajikistani Somoni', 'Turkmenistani Manat', 'Tunisian Dinar',
            'Tongan Paanga', 'Turkish Lira', 'Trinidad and Tobago Dollar',
            'New Taiwan Dollar', 'Tanzanian Shilling', 'Ukrainian Hryvnia',
            'Ugandan Shilling', 'United States Dollar', 'Uruguayan Peso',
            'Uzbekistan Som', 'Venezuelan Bolivar Fuerte', 'Vietnamese Dong',
            'Vanuatu Vatu', 'Samoan Tala', 'CFA Franc (BEAC)',
            'Troy Ounce of Silver', 'Troy Ounce of Gold',
            'East Caribbean Dollar', 'Special Drawing Rights',
            'CFA Franc (BCEAO)', 'Troy Ounce of Palladium', 'CFP Franc',
            'Troy Ounce of Platinum', 'Yemeni Rial', 'South African Rand',
            'Zambian Kwacha (pre-2013)', 'Zambian Kwacha', 'Zimbabwean Dollar']

    test_from(currency_from)
    test_to(currency_to)

    from urllib.request import urlopen
    web0 = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to\
    =EUR&amt=2.5'
    web = web0[0:web0.find('=') + 1] + currency_from + '&to=' + \
    currency_to + '&amt=' + str(amount_from)  # get the name of website
    doc = urlopen(web)
    docstr = doc.read()
    jstr = docstr.decode('ascii')
    start = jstr.find('''"to" : "''') + 8  # the output is always there.
    end = jstr.find(name[short.index(currency_to)]) - 1
    return(jstr[start:end])
    print(float(jstr[start:end]))  # find output number
    pass


def test():
    '''small tests so that the accuracy of exchage function is assured'''
    assert('28.497777' == exchange('USD','EUR',33))
    assert('110726.1222774' == exchange('CNY','LAK',89))
    assert('9728.333216482' == exchange('XPF','UGX',266))
    assert('42798.753629835' == exchange('JPY','MOP',589430))
    assert('0.99969822389463' == exchange('AWG','QAR',0.49216))
    assert('7.9159834803394E-7' == exchange('STD','SYP',0.00003236))
    print('All Tests Passed')



def main():
    """main module"""
    boolll = input('run_test_modules?please_enter"Y"or"N"')
    if boolll.upper() == 'Y':
        test()
    else:
        pass
    a = input('please_enter_"from"_type_currency, string_please.')
    b = input('please_enter_"to"_type_currency, string_please.')
    c = input('please_enter_the_amount_of_money, float_please.')
    exchange(str(a), str(b), str(c))


if __name__ == '__main__':
    main()
