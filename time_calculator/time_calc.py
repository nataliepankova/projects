def add_time(start, duration, dow = False):
  dow_index = {"monday": 0, "tuesday": 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
  dow_arr = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

  duration_tuple = duration.partition(":")
  dur_h = int(duration_tuple[0])
  dur_min = int(duration_tuple[2])

  start_tuple = start.partition(":")
  start_min_tuple = start_tuple[2].partition(" ")
  start_h = int(start_tuple[0])
  start_min = int(start_min_tuple[0])
  pod = start_min_tuple[2]
  pod_flip = {'AM': 'PM', 'PM': 'AM'}
  days = dur_h // 24

  #mins adjustment
  newmin = start_min + dur_min
  if newmin >= 60:
    start_h += 1
    newmin = newmin % 60
  #new hour formula
  newh = (start_h + dur_h) % 12
  #min and hour strings adjustment
  if newmin < 10:
    newmin = "0" + str(newmin)
  if newh == 0:
    newh = 12
  if pod == 'PM' and start_h + (dur_h % 12)>= 12:
    days += 1
  #dealing with pods
  pod_count = (start_h + dur_h) // 12
  if pod_count % 2 == 1:
    pod = pod_flip[pod]

  newtime = str(newh) + ':' + str(newmin) + ' ' + str(pod)

  if dow:
    #manages case problems of dow paramater
    dow = dow.lower()
    index = int(dow_index[dow] + days) % 7
    new_dow = dow_arr[index]
    newtime += ', ' + new_dow

  if days == 1:
    return newtime + " " + "(next day)"
  elif days > 1:
    return newtime  + " " + "(" + str(days) + ' days later)'

  return newtime
