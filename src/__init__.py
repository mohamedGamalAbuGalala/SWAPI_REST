import asyncio
from flask import Flask, request, jsonify
from src.utils.decorators import timing
from src.character.get_characters import get_characters

loop = asyncio.get_event_loop()
app = Flask(__name__)


# Flusk doesn't support asyncio https://stackoverflow.com/a/48491565/5055925
@app.route('/api/characters/', methods=['GET'])
@timing
def characters():
    try:
        name = request.args.get('name')

        if (name is None or len(name) == 0):
            return jsonify({'msg': 'You must pass a name'}), 400

        result = loop.run_until_complete(get_characters(name))

        if result == False:
            return jsonify({'msg': 'NotFound'})

        return jsonify(result)
    except:
        print('SERVER ERROR')
        return jsonify({'msg': 'INTERNAL_SERVER_ERROR'}), 500
