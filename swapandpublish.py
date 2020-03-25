from tableauhyperapi import *
from tableau_tools import *
from tableau_tools.tableau_documents import *
from getTokens import get_tableau_token
import tableauserverclient as TSC
import os


# note, please do not use file extensions
# comments indicate desired filetype
hypername = 'starwars' #.hyper
tdsxname = 'StarWars' #.tdsx
tdsxfilepath = '/Users/tsjoblad/Desktop/REST to Hyper (Github Version)/rest_to_hyper/' # file in this dir
serveraddress = 'https://us-west-2a.online.tableau.com/'
site_id = 'alpodev'
project_name = "Developer Platform"
tableau_token_name = 'tuckerToken'
tableau_token = get_tableau_token()


def gethypername():
    return hypername

def swap_hyper(logger_obj=None):
    '''Uses tableau_tools to open a local (shell) .tdsx file and replace the hyperfile.'''

    newly_built_hyper_filename = hypername + '.hyper'
    local_tds = TableauFileManager.open(
        filename=tdsxname + '.tdsx', logger_obj=logger_obj)
    filenames = local_tds.get_filenames_in_package()
    
    for filename in filenames:
        # Find my Hyper file
        if filename.find('.hyper') != -1:
            print("Overwritting Hyper...")
            local_tds.set_file_for_replacement(filename_in_package=filename,
                                            replacement_filname_on_disk=newly_built_hyper_filename)
            break

    local_tds.save_new_file(new_filename_no_extension=tdsxname + ' Updated')
    os.remove(tdsxname + ".tdsx")
    os.rename(tdsxname + " Updated.tdsx", tdsxname + ".tdsx")


def publishtoserver():
    '''Publishes updated, local .tdsx to Tableau, overwriting the original file.'''
    
    tableau_auth = TSC.PersonalAccessTokenAuth(
        token_name=tableau_token_name, personal_access_token=tableau_token, site_id=site_id)
    server = TSC.Server(serveraddress)

    with server.auth.sign_in(tableau_auth):
        all_projects, pagination_item = server.projects.get()

        for project in TSC.Pager(server.projects):
            if project.name == project_name:
                devplatproj = project.id

        if devplatproj is not None:
            print("Publishing...")
            overwrite_true = TSC.Server.PublishMode.Overwrite
            datasource = TSC.DatasourceItem(devplatproj)
            file_path = os.path.join(tdsxfilepath, tdsxname + '.tdsx')
            datasource = server.datasources.publish(
                datasource, file_path, overwrite_true)
