from time import gmtime, strftime
import platform
import checks

TMP_DIR = 'tmp'
SMTP_TO = 'add-your@mailadress.here'

SMTP_FROM = 'root@%s' % platform.node()
TIME = strftime('%Y-%m-%d %H:%M:%S', gmtime())

SUBJECT = dict()
SUBJECT['socket'] = 'ERROR connecting to %s:%s'
SUBJECT['url'] = 'ERROR getting URL %s'
SUBJECT['content'] = 'ERROR comparing content of %s'

BODY = dict()
BODY['socket'] = 'Host: %s\nDate: %s\n\nCould not connect to %s:%s\n\nError Message: %s' % (SMTP_FROM, TIME)
BODY['url'] = 'Host: %s\nDate: %s\n\nCould not open URL %s\n\nError Message: %s' % (SMTP_FROM, TIME)
BODY['content'] = 'Host: %s\nDate: %s\n\nThe content of URL %s differs too much!\n\nError Message: %s' % (SMTP_FROM, TIME)

FUNCTION = dict()
FUNCTION['socket'] = check_socket
FUNCTION['url'] = check_url
FUNCTION['content'] = check_url_content