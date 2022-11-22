import webapp3
import websocket
import json


class MainPage(webapp3.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')


class FetchData(webapp3.RequestHandler):
    def get(self):
        ws = websocket.WebSocket()
        ws.connect('ws://labapiprod.dinstation.dk/api/ws/departure/HH/')
        data = json.loads(ws.recv())
        ws.close()

        self.response.headers['Content-Type'] = 'text/plain'

        for train in data['data']['Trains']:
            self.response.write(f"#{train['TrainId']}, , Destination: {train['Routes'][0]['DestinationStationId']}, ScheduleTime: {train['ScheduleTime']}, IsCancelled: {train['IsCancelled']}, EstimatedTimeDeparture: {train['EstimatedTimeDeparture']}, DelayTime: {train['DelayTime']}, TrackCurrent: {train['TrackCurrent']}, TrackOriginal: {train['TrackOriginal']}\n")


app = webapp3.WSGIApplication([
    ('/', MainPage),
    ('/fetch', FetchData),
], debug=True)
