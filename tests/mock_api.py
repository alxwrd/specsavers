

class MockApi:

    def store_exists(self, store_name):
        return True

    def fetch_store_details(self, store_name):
        details = {
                'code': 200,
                'locale': 'gb_en',
                'content': {
                    'stores': [
                        {
                            'epos': 40,
                            'name': 'Nottingham - Wheelergate',
                            'business_type': 'opticians',
                            'url_name': 'nottingham',
                            'phone': {
                                'dialing_code': '+44',
                                'number': '0115 958 8361'
                                },
                            'address': {
                                'line1': '20-24 Wheeler Gate',
                                'line2': '',
                                'line3': '',
                                'town': 'Nottingham',
                                'county': 'Nottinghamshire',
                                'post_code': 'NG1 2ND'
                                },
                            'booking': {
                                'engine': 'sas',
                                'status': 'online'
                                },
                            'coordinate': {
                                'longitude': -1.149914,
                                'latitude': 52.952229
                                }
                            }
                        ]
                    }
                }
        return details

    def list_of_store_names(self, latitude, longitude):
        return ["woolwich", "barking", "eastham"]
