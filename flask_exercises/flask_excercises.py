from flask import Flask, request, jsonify

class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        users = {}

        @app.route("/user", methods=["POST"])
        def post():
            data = request.get_json()

            if 'name' not in data:
                response = {"name": "This field is required"}
                return jsonify(errors = response), 422  
            
            name = data['name']
            users[name] = {}

            return jsonify(data = f"User {name} is created!"), 201


        @app.route("/user/<name>", methods=["GET"])
        def get(name):
            if name in users:
                response = f"My name is {name}"
                return jsonify(data = response), 200
            
            return jsonify(''), 404

        @app.route("/user/<name>", methods=["PATCH"])
        def patch(name):
            if name in users:
                data = request.get_json()
                new_name = data["name"]
                users['name'] = new_name
                response = f"My name is {new_name}"
                return jsonify(data = response), 200
            
            return jsonify(''), 404

        @app.route("/user/<name>", methods=["DELETE"])
        def delete(name):
            if name in users:
                del users[name]
                return '', 204
            
            return jsonify(''), 404
