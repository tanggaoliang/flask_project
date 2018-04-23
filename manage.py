from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from exts import db
from tanggl import app

manager = Manager(app)

# 绑定app和db
migrate = Migrate(app, db)

# 添加迁移文件的命令到manage中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
