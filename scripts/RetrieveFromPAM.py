from collections import defaultdict

import pandas as pd
import numpy as np
import os


class BrowserRetrieve:

    @staticmethod
    def final_message(pam_result, version=None):

        if pam_result is not np.nan and pam_result.lower() not in ["ns", "na"]:
            return "Glad to say that we support your requirement for version {}".format(version)
        else:
            return "Oops. We don't support your requirement yet. Ask me if you have got anything more."

    def __init__(self, ):
        excel_path = os.getcwd()+os.sep+"my_data_sources"+os.sep+"PAM.xlsx"
        print("Initialization of data frames")
        global edc_browsers
        # edc_clients = pd.read_excel(excel_path, sheet_name='ClientSupport')
        edc_browsers = pd.read_excel(excel_path, sheet_name='BrowserSupport')
        # edc_datasources = pd.read_excel(excel_path, sheet_name='DataSourceSupport')
        # edc_globalisation = pd.read_excel(excel_path, sheet_name='Globalisation')

    def get_platforms(self):
        return ", ".join(edc_browsers.columns[2:].values)

    def get_browsers(self):
        return ", ".join(edc_browsers.Type.values)

    def get_value_from_df(self, df, index_type, col):
        error_msg = "Sorry!! Couldn't find anything in db matching your input. Please check again"
        try:
            print("Searching database....")
            result = df.loc[df['Type'].str.contains(index_type, case=False), col].values[0]
            version = df.loc[df['Type'].str.contains(index_type, case=False), "Version"].values[0]
            if result is None:
                return error_msg
            else:
                print("Fetched value.......", result)
                return BrowserRetrieve.final_message(result, version)
        except Exception as ex:
            print("Exception", str(ex))
            return error_msg


class ClientRetrieve:

    def __init__(self, ):
        print("Curr dir::",os.getcwd(),"Parent::",os.path.dirname(os.getcwd()))
        # excel_path = os.getcwd()+os.sep+"my_data_sources"+os.sep+"PAM.xlsx"
        excel_path =r"C:\Users\klvs\Downloads\GitProjects\rasa_bot_from_scratch\dummybot_v2\my_data_sources\PAM.xlsx"
        print("Initialization of data frames from file::",excel_path)
        global edc_clients
        edc_clients = pd.read_excel(excel_path, sheet_name='ClientSupport')
        # edc_browsers = pd.read_excel(excel_path, sheet_name='BrowserSupport')
        # edc_datasources = pd.read_excel(excel_path, sheet_name='DataSourceSupport')
        # edc_globalisation = pd.read_excel(excel_path, sheet_name='Globalisation')

    @staticmethod
    def get_client_from_mappings(val):
        print("Fetching clients from mappings for input::", val)
        mapping = val
        clients_mapping = {
            'PowerCenter Client 32bit 2': ['PowerCenter Client 32bit 2', 'pc', 'power center', 'power centre',
                                           'power center client'],
            'PowerExchange Navigator': ['PowerExchange Navigator', 'pwx'],
            'Informatica Developer Tool 64bit3': ['Informatica Developer Tool 64bit3', 'developer client', 'dev client',
                                                  'informatica client'],
            'Metadata Manager Agent': ['Metadata Manager Agent', 'mdm'],
            'EDC Agent': ['EDC Agent', 'edc', 'ldm', 'eic', 'edc client']}

        for k, v in clients_mapping.items():
            if val.lower() in v:
                mapping = k
                break
        return mapping

    @staticmethod
    def get_supported_versions(df, index, col):
        print("Fetching supported versions for\n", df, "::", index, "::", col)
        supported_versions = defaultdict(list)
        version_support_df = df.loc[
            df.Type.str.contains(index, case=False), ['Version', ClientRetrieve.get_client_from_mappings(col)]]
        # print("Version support df\n", version_support_df)
        version_support_dict = dict(
            zip(version_support_df['Version'], version_support_df[ClientRetrieve.get_client_from_mappings(col)]))
        # print("Version support dict", version_support_dict)
        for k, v in version_support_dict.items():
            if v is not np.nan and v.lower() not in ["ns", "na"]:
                supported_versions["s"].append(k)
            else:
                supported_versions["ns"].append(k)
        # print("supported versions", supported_versions)
        return dict(supported_versions)

    @staticmethod
    def final_message(pam_result, index=None, col=None):
        both_s_ns = "Here is the result. For the platform {} and client {}, we support these versions {} and dont support {}"
        only_s = "Here is the result. For the platform {} and client {}, we support these versions {}"
        only_ns = "Here is the result. We do not support any versions of the platform {} for client {}"

        if len(pam_result.keys()) > 1:
            return both_s_ns.format(index, col, pam_result.get('s'), pam_result.get('ns'))
        elif 's' in pam_result.keys():
            return only_s.format(index, col, pam_result.get('s'))
        elif 'ns' in pam_result.keys():
            return only_ns.format(index, col)
        else:
            return None

    @staticmethod
    def get_platforms():
        return ", ".join(set(edc_clients.Type.values))

    @staticmethod
    def get_clients():
        return ",".join(edc_clients.columns[2:].values)

    @staticmethod
    def get_value_from_df(df, index_type, col):
        error_msg = "Sorry!! Couldn't find anything in db matching your input. Please check again"
        try:
            print("Searching database for client support....")
            result = ClientRetrieve.get_supported_versions(df, index_type, col)
            # version = df.loc[df['Type'].str.contains(index_type, case=False), "Version"].values
            if result is None:
                return error_msg
            else:
                print("Fetched value.......", result)
                return ClientRetrieve.final_message(result, index_type, col)
        except Exception as ex:
            print("Exception", str(ex))
            return error_msg


if __name__ == '__main__':
    obj = ClientRetrieve()
    df = edc_clients
    index_type = 'windows'
    col = 'edc'
    # version = 'All'
    result = obj.get_value_from_df(df, index_type, col)
    print(result)
    # print(os.path.dirname(os.getcwd()))
