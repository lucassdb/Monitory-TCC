import cv2, threading, queue

class ThreadingClass:
  # initiate threading class
  def __init__(self, name):
    self.cap = cv2.VideoCapture(name)
    # define uma fila vazia e thread
    self.q = queue.Queue()
    t = threading.Thread(target=self._reader)
    t.daemon = True
    t.start()

  # leia os frames assim que estiverem disponíveis
  # esta abordagem remove o buffer interno do OpenCV e reduz o atraso do quadro
  def _reader(self):
    while True:
      ret, frame = self.cap.read() # read the frames and ---
      if not ret:
        break
      if not self.q.empty():
        try:
          self.q.get_nowait()
        except queue.Empty:
          pass
      self.q.put(frame) # --- armazene-os em uma fila (em vez do buffer)

  def read(self):
    return self.q.get() # busca quadros da fila um por um
