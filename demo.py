from rabbitmq_admin.api import AdminAPI

try:
    print('----------------------------Start LocalHost:15672-------------------------------')
    api = AdminAPI(url='http://localhost:15672', auth=('guest', 'guest'))
    api.create_vhost('second_vhost')
    api.create_user('admin', 'password')
    api.create_user_permission('admin', 'second_vhost')
    print(api.list_permissions())
    print('----------------------------Success-------------------------------')
except Exception as e:
    print('----------------------------Exception Localhost:15672-------------------------------')
    print(e)
