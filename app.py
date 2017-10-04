from main import server
from config import utils
from subprocess import call

call(['clear'])
call(['echo', 'Bonandos:/# This system is about to collect data from all machines in our intranet environment.'])
utils.generate_keys('main','client')
utils.package_folder('client/','packages/data_collector')
server.listen()
