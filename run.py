import threading

from flask import Flask
from thespian.actors import ActorSystem

from ActorCounter import TicketCounter
from TicketThread import TicketThread

app = Flask(__name__)

THREAD_COUNTER = 0
THREAD_AMOUNT_OF_TICKETS = 10000000
THREAD_LOCK = threading.Lock()
ACTOR_COUNTER = False


def next_ticket():
    global THREAD_COUNTER
    with THREAD_LOCK:
        THREAD_COUNTER += 1


def get_ticket():
    next_ticket()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/counter/thread')
def thread_counter():
    _ = TicketThread(get_ticket)
    return 'Thread Ticket is: %s' % THREAD_COUNTER


@app.route('/counter/actor')
def actor_counter():
    global ACTOR_COUNTER
    if not ACTOR_COUNTER:
        counter = ActorSystem().createActor(TicketCounter)
        response = ActorSystem().ask(counter, "What's my count?")
        ACTOR_COUNTER = counter
        return response
    else:
        response = ActorSystem().ask(ACTOR_COUNTER, "What's my count?")
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)