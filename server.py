from flask import Flask, jsonify, request
from models import Session, Message
from flask.views import MethodView

app = Flask('app')


class MessageView(MethodView):
    def get(self):
        session = Session()
        messages = session.query(Message).all()
        result = [msg.as_dict() for msg in messages]
        session.close()
        return jsonify(result)

    def post(self):
        data = request.get_json()
        message = Message(
            message_user=data['user'],
            message_headers=data['headers'],
            message_text=data['text']
        )
        session = Session()
        session.add(message)
        session.commit()
        result = message.__dict__
        session.close()
        return "Создано сообщение"

    def delete(self, message_id):
        session = Session()
        message = session.query(Message).filter(Message.id == message_id).first()
        if message:
            session.delete(message)
            session.commit()
            session.close()
            return jsonify({'message': 'Сообщение удалено'})
        else:
            session.close()
            return jsonify({'error': 'Сообщение не найдено'})


class IndexView(MethodView):
    def get(self):
        return 'Главная страница'

    def post(self):
        pass

    def delete(self):
        pass


message_view = MessageView.as_view('message')

app.add_url_rule('/', view_func=IndexView.as_view('index'))
app.add_url_rule('/message/<int:message_id>', view_func=message_view)
app.add_url_rule('/message', view_func=message_view)
if __name__ == "__main__":
    app.run()
