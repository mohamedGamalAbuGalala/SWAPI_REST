import asyncio
from flask import Flask, request, jsonify
from decorators import timing
from character.get_characters import get_characters

loop = asyncio.get_event_loop()
app = Flask(__name__)


# Flusk doesn't support asyncio https://stackoverflow.com/a/48491565/5055925
@app.route('/characters/', methods=['GET'])
@timing
def characters():
    # try:
    name = request.args.get('name')

    if (name is None):
        return jsonify({'msg': 'You must pass a name'}), 400

    result = loop.run_until_complete(get_characters(name))

    if result == False:
        return jsonify({'msg': 'NotFound'})

    return jsonify(result)

    # except:
    #     print('SERVER ERROR')
    #     return jsonify({'msg': 'INTERNAL_SERVER_ERROR'}), 500


if __name__ == "__main__":
    app.run()
    # TODO: remove debug mode
    # app.run(debug=True)
