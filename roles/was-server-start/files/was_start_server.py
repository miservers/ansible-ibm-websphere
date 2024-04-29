# Start a WAS Server
#  $WAS_INSTALL_ROOT/profiles/Dmgr01/bin/wsadmin.sh -lang jython -conntype SOAP -host rhel2 \
#                                                 -username wasadmin -password changeit \
#		            							 -f was_create_server.py serverName nodeName cellName
#
#
import sys

def getServerObj(_server, _node, _cell):
  serverObj = AdminControl.completeObjectName('cell=%s,node=%s,name=%s,type=Server,*'%(_cell, _node, _server))
  return serverObj


def getServerState(_server, _node, _cell):
  serverObj = getServerObj(_server, _node, _cell)

  if len(serverObj) > 0:
    serverState = AdminControl.getAttribute(serverObj, 'state')
  else:
    serverState = 'STOPPED'
  
  return serverState

def startServer(_server, _node, _cell):
  serverState = getServerState (_server, _node, _cell)

  if serverState != 'STARTED':
    AdminControl.startServer(_server, _node)
    print 'Server Started'
  else:
    print 'Warning, Server already:'+serverState

def stopServer(_server, _node, _cell):
  serverState = getServerState (_server, _node, _cell)

  if serverState == 'STARTED':
    AdminControl.stopServer(_server, _node)
    print 'Server Stopped'
  else:
    print 'Warning, Server not already STARTED, current state is '+serverState

## MAIN
_server = sys.argv[0]
_node = sys.argv[1]
_cell = sys.argv[2]

startServer(_server, _node, _cell)

