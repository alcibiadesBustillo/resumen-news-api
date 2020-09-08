import logging
logging.basicConfig(level=logging.INFO)
import subprocess

logger = logging.getLogger(__name__)
news_sites_uids = ['newyorktimes']

def main():
    _extract()
    _transform()
    _load()

def _extract():
    logger.info('Starting extract process')
    for news_sites_uid in news_sites_uids:
        subprocess.run(['python', 'main.py', news_sites_uid], cwd='./extract')
        subprocess.run(['find', '.', '-name', '{}*'.format(news_sites_uid), 
                        '-exec', 'mv', '{}', '../transform/{}_.csv'.format(news_sites_uid),
                        ';'], cwd='./extract')

def _transform():
    logger.info('Starting transform process')
    for news_sites_uid in news_sites_uids:
        dirty_data_filename = '{}_.csv'.format(news_sites_uid)
        clean_data_filename = 'clean_{}'.format(dirty_data_filename)
        subprocess.run(['python', 'main.py', dirty_data_filename], cwd='./transform')
        subprocess.run(['rm', dirty_data_filename], cwd='./transform')
        subprocess.run(['mv', clean_data_filename, '../load/{}.csv'.format(news_sites_uid)],
                        cwd='./transform'
        )          

def _load():
    logger.info('Starting load process')
    for news_sites_uid in news_sites_uids:
        clean_data_filename = '{}.csv'.format(news_sites_uid)
        subprocess.run(['python', 'main.py', clean_data_filename], cwd='./load')
        subprocess.run(['rm', clean_data_filename], cwd='./load')


if __name__ == '__main__':
    main() 


