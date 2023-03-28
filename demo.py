from rabbitmq_admin.api import AdminAPI
# api = AdminAPI(url='http://192.168.99.101:15672', auth=('guest', 'guest'))
# api.create_vhost('second_vhost')
# api.create_user('admin', 'password')
# api.create_user_permission('admin', 'second_vhost')
# api.list_permission()

# print('----------------------------FINISHED-------------------------------')


try:
    print('----------------------------Start LocalHost:15672-------------------------------')
    api = AdminAPI(url='http://localhost:15672', auth=('guest', 'guest'))
    api.create_vhost('second_vhost')
    api.create_user('admin', 'password')
    api.create_user_permission('admin', 'second_vhost')
    api.list_permission()
    print('----------------------------FINISHED-------------------------------')
except Exception as e:
    print('----------------------------Exception Localhost:15672-------------------------------')
    print(e)

print('\n\n')

try:
    print('----------------------------Start LocalHost:5672-------------------------------')
    api = AdminAPI(url='http://localhost:5672', auth=('guest', 'guest'))
    api.create_vhost('second_vhost')
    api.create_user('admin', 'password')
    api.create_user_permission('admin', 'second_vhost')
    api.list_permission()
    print('----------------------------FINISHED-------------------------------')
except Exception as e:
    print('----------------------------Exception Localhost:5672-------------------------------')
    print(e)