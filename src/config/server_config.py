# wsadmin script generated by binaryAppScanner
# This configuration was migrated on 2020-06-26 at 15:38:30 from the following location: /opt/IBM/WebSphere/AppServer/profiles/AppSrv01
# The binary scanner does not support the migration of all WebSphere traditional configuration elements. Check the binary scanner documentation for the list of supported configuration elements.

Cell=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/')
Node=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/Node:' + AdminControl.getNode() + '/')
Server=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/Node:' + AdminControl.getNode() + '/Server:server1')
NodeName=AdminControl.getNode()

print 'Starting Creating JVM Properties'
# Properties are migrated from server workstationNode01/server1.
AdminTask.setJVMSystemProperties(["-propertyName", "com.ibm.security.jgss.debug", "-propertyValue", "off"])
AdminTask.setJVMSystemProperties(["-propertyName", "com.ibm.security.krb5.Krb5Debug", "-propertyValue", "off"])

print 'Starting Creating Authentication Alias'

print 'Starting Creating Queues'

print 'Starting Creating Topics'

print 'Starting Creating Activation Specifications'

print 'Starting Creating Connection Factories'

print 'Starting Creating JDBC Providers'

print 'Starting Creating Variables'

print 'Starting Saving Configuration Changes Before Application Deployment'
AdminConfig.save()
print 'Starting Application Deployment'
AdminConfig.create('Library', Server, [['name', 'globalSharedLibrary'], ['classPath',  '/work/config/lib']])
appServer = AdminConfig.list('ApplicationServer',Server)
classLoader1 = AdminConfig.create('Classloader', appServer, [['mode',  'PARENT_FIRST']])
AdminConfig.create('LibraryRef', classLoader1, [['libraryName', 'globalSharedLibrary']])
#AdminApp.install('/path/to/modresorts-1.0.war', ["-node", NodeName, "-server", "server1", "-appname", "modresorts-1.0.war", "-contextroot", "/resorts", "-CtxRootForWebMod", [["modresorts-1.0.war", "modresorts-1.0.war,WEB-INF/web.xml", "/resorts"]]])
AdminConfig.save()
