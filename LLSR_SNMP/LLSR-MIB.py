# PySNMP SMI module. Autogenerated from smidump -f python LLSR-MIB
# by libsmi2pysnmp-0.1.3 at Tue Nov 15 15:14:21 2016,
# Python version sys.version_info(major=2, minor=7, micro=12, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( netSnmpPlaypen, ) = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpPlaypen")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DateAndTime, DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString")

# Objects

llsr = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 9999, 9999, 1)).setRevisions(("2016-09-21 00:00",))
if mibBuilder.loadTexts: llsr.setOrganization("scs.carleton.ca")
if mibBuilder.loadTexts: llsr.setContactInfo("email:    wenqianwang@scs.carleton.ca")
if mibBuilder.loadTexts: llsr.setDescription("Remote Monitoring MIB for Underwater Acoustic Sensor Networks")
nodeStatsTable = MibTable((1, 3, 6, 1, 4, 1, 8072, 9999, 9999, 1, 1))
if mibBuilder.loadTexts: nodeStatsTable.setDescription("The table for putting nodestatus")
nodeStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 9999, 9999, 1, 1, 1)).setIndexNames((0, "LLSR-MIB", "index"))
if mibBuilder.loadTexts: nodeStatsEntry.setDescription("A collection of node statistics kept for a node")
index = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 9999, 9999, 1, 1, 1, 1), Unsigned32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: index.setDescription("index")
nodeAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 9999, 9999, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeAddr.setDescription("The node address")
maxAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 9999, 9999, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: maxAttempts.setDescription("The max retry")
broadcastInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 9999, 9999, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: broadcastInterval.setDescription("broadcast interval")
mgmtMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 9999, 9999, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgmtMode.setDescription("MgmtMode, 0->Manual, 1->Bio")
lastUpdated = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 9999, 9999, 1, 1, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastUpdated.setDescription("lastupdated item")
lastUpdatedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 9999, 9999, 1, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastUpdatedTime.setDescription("lastupdated time UTC format")
mgmtInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 9999, 9999, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmtInfo.setDescription("RowStatus, 0->nodealive, 1->requestsent, 2->itemupdated, 3->mgmtError, 4->nodedead")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("LLSR-MIB", PYSNMP_MODULE_ID=llsr)

# Objects
mibBuilder.exportSymbols("LLSR-MIB", llsr=llsr, nodeStatsTable=nodeStatsTable, nodeStatsEntry=nodeStatsEntry, index=index, nodeAddr=nodeAddr, maxAttempts=maxAttempts, broadcastInterval=broadcastInterval, mgmtMode=mgmtMode, lastUpdated=lastUpdated, lastUpdatedTime=lastUpdatedTime, mgmtInfo=mgmtInfo)

