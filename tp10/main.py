from celery import Celery



def main():
    app = Celery('tasks', broker='pyamqp://guest@localhost//',backend="rpc://")
    result = app.send_task('tasks.hello')
    print(result.get())
    result = app.send_task('tasks.add',args=(2,3))
    print(result.get())


if __name__=='__main__':
    main()
