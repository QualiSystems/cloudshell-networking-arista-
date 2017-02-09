# PySNMP SMI module. Autogenerated from smidump -f python ARISTA-PRODUCTS-MIB
# by libsmi2pysnmp-0.1.3 at Tue Jan 31 10:06:37 2017,
# Python version sys.version_info(major=2, minor=7, micro=6, releaselevel='final', serial=0)

# Imports

( aristaModules, aristaProducts, ) = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaModules", "aristaProducts")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks")

# Objects

aristaCVX = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 2682))
aristaDCS7010T48 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7010, 427, 48))
aristaDCS7010T48DC = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7010, 427, 48, 2957))
aristaDCS7048T4S = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7048, 427, 4, 3282))
aristaDCS7048TA = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7048, 427, 3648))
aristaDCS7050T36 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 427, 36))
aristaDCS7050T52 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 427, 52))
aristaDCS7050T52SSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 427, 52, 761))
aristaDCS7050T64 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 427, 64))
aristaDCS7050T64SSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 427, 64, 761))
aristaDCS7050TX48 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 48))
aristaDCS7050TX48SSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 48, 761))
aristaDCS7050TX64 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 64))
aristaDCS7050TX64SSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 64, 761))
aristaDCS7050TX72 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 72))
aristaDCS7050TX72SSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 72, 761))
aristaDCS7050TX72Q = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 72, 2512))
aristaDCS7050TX72QSSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 72, 2512, 761))
aristaDCS7050TX96 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 96))
aristaDCS7050TX96SSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 96, 761))
aristaDCS7050TX128 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 128))
aristaDCS7050TX128SSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 128, 761))
aristaDCS7050Q16 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 2512, 16))
aristaDCS7050Q16SSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 2512, 16, 761))
aristaDCS7050QX32 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 32))
aristaDCS7050QX32SSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 32, 761))
aristaDCS7050QX32CLSSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 32, 2745, 761))
aristaDCS7050QX32S = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 32, 3282))
aristaDCS7050QX32SSSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 32, 3282, 761))
aristaDCS7050S52 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3282, 52))
aristaDCS7050S52SSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3282, 52, 761))
aristaDCS7050S64 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3282, 64))
aristaDCS7050S64SSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3282, 64, 761))
aristaDCS7050SX64 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 64))
aristaDCS7050SX64SSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 64, 761))
aristaDCS7050SX72 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 72))
aristaDCS7050SX72SSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 72, 761))
aristaDCS7050SX72Q = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 72, 2512))
aristaDCS7050SX72QSSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 72, 2512, 761))
aristaDCS7050SX96 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 96))
aristaDCS7050SX96SSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 96, 761))
aristaDCS7050SX128 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 128))
aristaDCS7050SX128SSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 128, 761))
aristaDCS7120T4S = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7120, 427, 4, 3282))
aristaDCS7124FX = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7124, 2312))
aristaDCS7124FXCL = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7124, 2312, 2745))
aristaDCS7124S = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7124, 3282))
aristaDCS7124SX = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7124, 3741))
aristaDCS7124SXSSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7124, 3741, 761))
aristaDCS7140T8S = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7140, 427, 8, 3282))
aristaDCS7148S = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7148, 3282))
aristaDCS7148SX = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7148, 3741))
aristaDCS7150S24 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 24))
aristaDCS7150S24CL = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 24, 2745))
aristaDCS7150S24CLSSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 24, 2745, 761))
aristaDCS7150S52CL = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 52, 2745))
aristaDCS7150S52CLSSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 52, 2745, 761))
aristaDCS7150S64CL = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 64, 2745))
aristaDCS7150S64CLSSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 64, 2745, 761))
aristaDCS7250QX64 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7250, 3095, 64))
aristaDCS7250QX64SSD = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7250, 3095, 64, 761))
aristaDCS7250QX64M = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7250, 3095, 64, 972))
aristaDCS7280SE64 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3714, 64))
aristaDCS7280SE68 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3714, 68))
aristaDCS7280SE72 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3714, 72))
aristaDCS7304 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7304))
aristaDCS7308 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7308))
aristaDCS7316 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7316))
aristaDCS7504 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7504))
aristaDCS7504N = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7504, 1359))
aristaDCS7508 = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7508))
aristaDCS7508N = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7508, 1359))
aristaProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 2, 1)).setRevisions(("2015-10-28 00:00","2015-09-15 00:00","2015-06-03 00:00","2015-05-27 00:00","2015-04-20 00:00","2015-03-19 00:00","2014-12-02 00:00","2014-08-15 00:00","2014-07-31 09:30","2014-07-18 09:00","2014-05-19 16:00","2014-04-08 16:00","2014-04-04 16:09","2014-04-04 16:08","2014-04-02 12:00","2014-04-02 11:00","2014-03-11 16:00","2014-01-02 16:00","2014-01-01 09:00","2013-11-24 09:30","2013-11-24 09:00","2013-11-24 08:30","2013-11-24 08:00","2013-11-23 12:00","2013-11-23 11:30","2013-11-23 11:00","2013-11-19 08:00","2013-11-13 08:00","2013-11-01 08:00","2013-10-02 08:00","2013-09-26 11:20","2013-06-08 08:00","2013-01-26 08:00","2012-12-12 12:12","2012-11-28 08:00","2012-09-03 08:00","2012-08-31 08:00","2012-04-17 08:00","2012-04-03 08:00","2012-03-09 08:00","2012-02-20 08:00","2012-02-01 08:00","2011-09-01 08:00","2011-08-29 08:00","2011-08-04 08:00","2011-07-16 14:00","2011-06-22 18:00","2011-03-31 13:00","2011-02-24 08:00","2010-10-24 16:00","2010-09-17 20:40","2010-04-05 09:42","2010-04-05 09:41","2009-06-08 15:58","2009-04-17 15:05","2008-09-10 14:15","2008-03-03 12:30",))
if mibBuilder.loadTexts: aristaProductsMIB.setOrganization("Arista Networks, Inc.")
if mibBuilder.loadTexts: aristaProductsMIB.setContactInfo("Arista Networks, Inc.\n\nPostal: 5453 Great America Parkway\n        Santa Clara, CA 95054\n\nTel: +1 408 547-5500\n\nE-mail: snmp@arista.com")
if mibBuilder.loadTexts: aristaProductsMIB.setDescription("This module defines the object identifiers returned as values for\nsysObjectID or entPhysicalVendorType for Arista Networks hardware.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("ARISTA-PRODUCTS-MIB", PYSNMP_MODULE_ID=aristaProductsMIB)

# Objects
mibBuilder.exportSymbols("ARISTA-PRODUCTS-MIB", aristaCVX=aristaCVX, aristaDCS7010T48=aristaDCS7010T48, aristaDCS7010T48DC=aristaDCS7010T48DC, aristaDCS7048T4S=aristaDCS7048T4S, aristaDCS7048TA=aristaDCS7048TA, aristaDCS7050T36=aristaDCS7050T36, aristaDCS7050T52=aristaDCS7050T52, aristaDCS7050T52SSD=aristaDCS7050T52SSD, aristaDCS7050T64=aristaDCS7050T64, aristaDCS7050T64SSD=aristaDCS7050T64SSD, aristaDCS7050TX48=aristaDCS7050TX48, aristaDCS7050TX48SSD=aristaDCS7050TX48SSD, aristaDCS7050TX64=aristaDCS7050TX64, aristaDCS7050TX64SSD=aristaDCS7050TX64SSD, aristaDCS7050TX72=aristaDCS7050TX72, aristaDCS7050TX72SSD=aristaDCS7050TX72SSD, aristaDCS7050TX72Q=aristaDCS7050TX72Q, aristaDCS7050TX72QSSD=aristaDCS7050TX72QSSD, aristaDCS7050TX96=aristaDCS7050TX96, aristaDCS7050TX96SSD=aristaDCS7050TX96SSD, aristaDCS7050TX128=aristaDCS7050TX128, aristaDCS7050TX128SSD=aristaDCS7050TX128SSD, aristaDCS7050Q16=aristaDCS7050Q16, aristaDCS7050Q16SSD=aristaDCS7050Q16SSD, aristaDCS7050QX32=aristaDCS7050QX32, aristaDCS7050QX32SSD=aristaDCS7050QX32SSD, aristaDCS7050QX32CLSSD=aristaDCS7050QX32CLSSD, aristaDCS7050QX32S=aristaDCS7050QX32S, aristaDCS7050QX32SSSD=aristaDCS7050QX32SSSD, aristaDCS7050S52=aristaDCS7050S52, aristaDCS7050S52SSD=aristaDCS7050S52SSD, aristaDCS7050S64=aristaDCS7050S64, aristaDCS7050S64SSD=aristaDCS7050S64SSD, aristaDCS7050SX64=aristaDCS7050SX64, aristaDCS7050SX64SSD=aristaDCS7050SX64SSD, aristaDCS7050SX72=aristaDCS7050SX72, aristaDCS7050SX72SSD=aristaDCS7050SX72SSD, aristaDCS7050SX72Q=aristaDCS7050SX72Q, aristaDCS7050SX72QSSD=aristaDCS7050SX72QSSD, aristaDCS7050SX96=aristaDCS7050SX96, aristaDCS7050SX96SSD=aristaDCS7050SX96SSD, aristaDCS7050SX128=aristaDCS7050SX128, aristaDCS7050SX128SSD=aristaDCS7050SX128SSD, aristaDCS7120T4S=aristaDCS7120T4S, aristaDCS7124FX=aristaDCS7124FX, aristaDCS7124FXCL=aristaDCS7124FXCL, aristaDCS7124S=aristaDCS7124S, aristaDCS7124SX=aristaDCS7124SX, aristaDCS7124SXSSD=aristaDCS7124SXSSD, aristaDCS7140T8S=aristaDCS7140T8S, aristaDCS7148S=aristaDCS7148S, aristaDCS7148SX=aristaDCS7148SX, aristaDCS7150S24=aristaDCS7150S24, aristaDCS7150S24CL=aristaDCS7150S24CL, aristaDCS7150S24CLSSD=aristaDCS7150S24CLSSD, aristaDCS7150S52CL=aristaDCS7150S52CL, aristaDCS7150S52CLSSD=aristaDCS7150S52CLSSD, aristaDCS7150S64CL=aristaDCS7150S64CL, aristaDCS7150S64CLSSD=aristaDCS7150S64CLSSD, aristaDCS7250QX64=aristaDCS7250QX64, aristaDCS7250QX64SSD=aristaDCS7250QX64SSD, aristaDCS7250QX64M=aristaDCS7250QX64M, aristaDCS7280SE64=aristaDCS7280SE64, aristaDCS7280SE68=aristaDCS7280SE68, aristaDCS7280SE72=aristaDCS7280SE72, aristaDCS7304=aristaDCS7304, aristaDCS7308=aristaDCS7308, aristaDCS7316=aristaDCS7316, aristaDCS7504=aristaDCS7504, aristaDCS7504N=aristaDCS7504N, aristaDCS7508=aristaDCS7508, aristaDCS7508N=aristaDCS7508N, aristaProductsMIB=aristaProductsMIB)

