import websocket
import json

ws = websocket.WebSocket()
ws.connect('ws://labapiprod.dinstation.dk/api/ws/departure/HH/')
data = json.loads(ws.recv())
ws.close()

for train in data['data']['Trains']:
    # print(train)
    print(f"#{train['TrainId']}, Destination: {train['Routes'][0]['DestinationStationId']}, ScheduleTime: {train['ScheduleTime']}, IsCancelled: {train['IsCancelled']}, EstimatedTimeDeparture: {train['EstimatedTimeDeparture']}, DelayTime: {train['DelayTime']}, TrackCurrent: {train['TrackCurrent']}, TrackOriginal: {train['TrackOriginal']}")
    break
