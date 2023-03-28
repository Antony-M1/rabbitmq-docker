from rabbitmq_admin.api import AdminAPI
api = AdminAPI(url='http://192.168.99.101:15672', auth=('guest', 'guest'))
api.create_vhost('second_vhost')
api.create_user('admin', 'password')
api.create_user_permission('admin', 'second_vhost')
api.list_permission()