def parseCanvasSize(string):
  size = string.split(':')[1]
  width, height = map(int, size.split(' x '))
  return width, height

def parseBackgroundColor(string):
  hex_color = string.split(':')[1].strip()
  return hex_color

def parseFrameCount(string):
  count = int(string.split(':')[1])
  return count

def parseAttrOrder(string):
  return list(map(lambda x: x.strip(), string.split(':')[1].split()))

def parseFrameAttr(frameCount, attrList, string):
  attr = list(map(lambda x: x.strip(), string.split(':')[1].split()))
  return {
    'width': int(attr[attrList.index('width')]),
    'height': int(attr[attrList.index('height')]),
    'alpha': 1 if attr[attrList.index('alpha')] == 'yes' else 0,
    'duration': int(attr[attrList.index('duration')])
  }

canvasWidth, canvasHeight = parseCanvasSize(input())
backgroundColor = parseBackgroundColor(input())
frameCount = parseFrameCount(input())

print(canvasWidth)
print(canvasHeight)
print(int(backgroundColor, 0))
print(frameCount)

attrList = parseAttrOrder(input())
for _ in range(0, frameCount):
  attr = parseFrameAttr(frameCount, attrList, input())
  print("%dx%d, %d, %d" % (attr['width'], attr['height'], attr['duration'], attr['alpha']))