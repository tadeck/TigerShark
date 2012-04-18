#
# Generated by TigerShark.tools.convertPyX12 on 2012-04-05 18:33:56.399880
#
from tigershark.X12.parse import Message, Loop, Segment, Composite, Element, Properties
parsed_841_1100 = Loop( u'1100', Properties(looptype='',repeat=u'>1',pos=u'010',req_sit=u'R',desc=u'Code List Source'), 
Segment( u'N1', Properties(syntax=u'R0203 P0304',req_sit=u'S',repeat=u'1',pos=u'120',desc=u'Code List Source'),
  Element( u'N101', Properties(desc=u'Entity Identifier Code', req_sit=u'R', data_type=(u'ID',u'2',u'3'), position=1,
    codes=[u'0F'] ) ),
  Element( u'N102', Properties(desc=u'Name', req_sit=u'R', data_type=(u'AN',u'1',u'60'), position=2,
    codes=[] ) ),
  Element( u'N103', Properties(desc=u'Identification Code Qualifier', req_sit=u'N', data_type=(u'ID',u'1',u'2'), position=3,
    codes=[] ) ),
  Element( u'N104', Properties(desc=u'Identification Code', req_sit=u'N', data_type=(u'AN',u'2',u'80'), position=4,
    codes=[] ) ),
  Element( u'N105', Properties(desc=u'Entity Relationship Code', req_sit=u'N', data_type=(u'ID',u'2',u'2'), position=5,
    codes=[] ) ),
  Element( u'N106', Properties(desc=u'Entity Identifier Code', req_sit=u'N', data_type=(u'ID',u'2',u'3'), position=6,
    codes=[] ) ),
),
)
parsed_841_1000 = Loop( u'1000', Properties(looptype='',repeat=u'>1',pos=u'010',req_sit=u'R',desc=u'Code List'), 
Segment( u'SPI', Properties(syntax=u'P0203',req_sit=u'R',repeat=u'1',pos=u'020',desc=u'Code List'),
  Element( u'SPI01', Properties(desc=u'Security Level Code', req_sit=u'R', data_type=(u'ID',u'2',u'2'), position=1,
    codes=[u'00'] ) ),
  Element( u'SPI02', Properties(desc=u'Reference Identification Qualifier', req_sit=u'N', data_type=(u'ID',u'2',u'3'), position=2,
    codes=[] ) ),
  Element( u'SPI03', Properties(desc=u'Reference Identification', req_sit=u'N', data_type=(u'AN',u'1',u'30'), position=3,
    codes=[] ) ),
  Element( u'SPI04', Properties(desc=u'Entity Title', req_sit=u'R', data_type=(None,None,None), position=4,
    codes=[] ) ),
  Element( u'SPI05', Properties(desc=u'Entity Purpose', req_sit=u'R', data_type=(None,None,None), position=5,
    codes=[] ) ),
  Element( u'SPI06', Properties(desc=u'Entity Status Code', req_sit=u'N', data_type=(None,None,None), position=6,
    codes=[] ) ),
  Element( u'SPI07', Properties(desc=u'Transaction Set Purpose Code', req_sit=u'N', data_type=(u'ID',u'2',u'2'), position=7,
    codes=[] ) ),
  Element( u'SPI08', Properties(desc=u'Report Type Code', req_sit=u'N', data_type=(u'ID',u'2',u'2'), position=8,
    codes=[] ) ),
  Element( u'SPI09', Properties(desc=u'Security Level Code', req_sit=u'N', data_type=(u'ID',u'2',u'2'), position=9,
    codes=[] ) ),
  Element( u'SPI10', Properties(desc=u'Agency Qualifier Code', req_sit=u'N', data_type=(u'ID',u'2',u'2'), position=10,
    codes=[] ) ),
  Element( u'SPI11', Properties(desc=u'Source Subqualifier', req_sit=u'N', data_type=(u'AN',u'1',u'15'), position=11,
    codes=[] ) ),
  Element( u'SPI12', Properties(desc=u'Assigned Number', req_sit=u'N', data_type=(u'N0',u'1',u'6'), position=12,
    codes=[] ) ),
  Element( u'SPI13', Properties(desc=u'Certification Type Code', req_sit=u'N', data_type=(u'ID',u'1',u'1'), position=13,
    codes=[] ) ),
  Element( u'SPI14', Properties(desc=u'Proposal Data Detail Identifier Code', req_sit=u'N', data_type=(None,None,None), position=14,
    codes=[] ) ),
  Element( u'SPI15', Properties(desc=u'Hierarchical Structure Code', req_sit=u'N', data_type=(u'ID',u'4',u'4'), position=15,
    codes=[] ) ),
),
Segment( u'RDT', Properties(syntax=u'C0102 L030405 C0605',req_sit=u'R',repeat=u'>1',pos=u'030',desc=u'Release Date'),
  Element( u'RDT01', Properties(desc=u'Revision Level Code', req_sit=u'N', data_type=(None,None,None), position=1,
    codes=[] ) ),
  Element( u'RDT02', Properties(desc=u'Revision Value', req_sit=u'N', data_type=(None,None,None), position=2,
    codes=[] ) ),
  Element( u'RDT03', Properties(desc=u'Date/Time Qualifier', req_sit=u'R', data_type=(u'ID',u'3',u'3'), position=3,
    codes=[u'171'] ) ),
  Element( u'RDT04', Properties(desc=u'Date', req_sit=u'R', data_type=(u'DT',u'8',u'8'), position=4,
    codes=[] ) ),
  Element( u'RDT05', Properties(desc=u'Time', req_sit=u'N', data_type=(u'TM',u'4',u'8'), position=5,
    codes=[] ) ),
  Element( u'RDT06', Properties(desc=u'Time Code', req_sit=u'N', data_type=(u'ID',u'2',u'2'), position=6,
    codes=[] ) ),
),
Segment( u'RDT', Properties(syntax=u'C0102 L030405 C0605',req_sit=u'S',repeat=u'1',pos=u'030',desc=u'Effective Date'),
  Element( u'RDT01', Properties(desc=u'Revision Level Code', req_sit=u'N', data_type=(None,None,None), position=1,
    codes=[] ) ),
  Element( u'RDT02', Properties(desc=u'Revision Value', req_sit=u'N', data_type=(None,None,None), position=2,
    codes=[] ) ),
  Element( u'RDT03', Properties(desc=u'Date/Time Qualifier', req_sit=u'R', data_type=(u'ID',u'3',u'3'), position=3,
    codes=[u'007'] ) ),
  Element( u'RDT04', Properties(desc=u'Date', req_sit=u'R', data_type=(u'DT',u'8',u'8'), position=4,
    codes=[] ) ),
  Element( u'RDT05', Properties(desc=u'Time', req_sit=u'N', data_type=(u'TM',u'4',u'8'), position=5,
    codes=[] ) ),
  Element( u'RDT06', Properties(desc=u'Time Code', req_sit=u'N', data_type=(u'ID',u'2',u'2'), position=6,
    codes=[] ) ),
),
parsed_841_1100,
)
parsed_841_HEADER = Loop( u'HEADER', Properties(looptype=u'wrapper',repeat=u'1',pos=u'010',req_sit=u'R',desc=u'Table 1 - Header'), 
parsed_841_1000,
)
parsed_841_2100 = Loop( u'2100', Properties(looptype='',repeat=u'>1',pos=u'010',req_sit=u'R',desc=u'Code List Value and Definition'), 
Segment( u'SPI', Properties(syntax=u'P0203',req_sit=u'R',repeat=u'1',pos=u'020',desc=u'Code List Value and Definition'),
  Element( u'SPI01', Properties(desc=u'Security Level Code', req_sit=u'R', data_type=(u'ID',u'2',u'2'), position=1,
    codes=[u'00'] ) ),
  Element( u'SPI02', Properties(desc=u'Reference Identification Qualifier', req_sit=u'R', data_type=(u'ID',u'2',u'3'), position=2,
    codes=[u'ZZ'] ) ),
  Element( u'SPI03', Properties(desc=u'Reference Identification', req_sit=u'R', data_type=(u'AN',u'1',u'30'), position=3,
    codes=[] ) ),
  Element( u'SPI04', Properties(desc=u'Entity Title', req_sit=u'R', data_type=(None,None,None), position=4,
    codes=[] ) ),
  Element( u'SPI05', Properties(desc=u'Entity Purpose', req_sit=u'N', data_type=(None,None,None), position=5,
    codes=[] ) ),
  Element( u'SPI06', Properties(desc=u'Entity Status Code', req_sit=u'N', data_type=(None,None,None), position=6,
    codes=[] ) ),
  Element( u'SPI07', Properties(desc=u'Transaction Set Purpose Code', req_sit=u'N', data_type=(u'ID',u'2',u'2'), position=7,
    codes=[] ) ),
  Element( u'SPI08', Properties(desc=u'Report Type Code', req_sit=u'N', data_type=(u'ID',u'2',u'2'), position=8,
    codes=[] ) ),
  Element( u'SPI09', Properties(desc=u'Security Level Code', req_sit=u'N', data_type=(u'ID',u'2',u'2'), position=9,
    codes=[] ) ),
  Element( u'SPI10', Properties(desc=u'Agency Qualifier Code', req_sit=u'N', data_type=(u'ID',u'2',u'2'), position=10,
    codes=[] ) ),
  Element( u'SPI11', Properties(desc=u'Source Subqualifier', req_sit=u'N', data_type=(u'AN',u'1',u'15'), position=11,
    codes=[] ) ),
  Element( u'SPI12', Properties(desc=u'Assigned Number', req_sit=u'N', data_type=(u'N0',u'1',u'6'), position=12,
    codes=[] ) ),
  Element( u'SPI13', Properties(desc=u'Certification Type Code', req_sit=u'N', data_type=(u'ID',u'1',u'1'), position=13,
    codes=[] ) ),
  Element( u'SPI14', Properties(desc=u'Proposal Data Detail Identifier Code', req_sit=u'N', data_type=(None,None,None), position=14,
    codes=[] ) ),
  Element( u'SPI15', Properties(desc=u'Hierarchical Structure Code', req_sit=u'N', data_type=(u'ID',u'4',u'4'), position=15,
    codes=[] ) ),
),
Segment( u'MSG', Properties(syntax=u'C0302',req_sit=u'S',repeat=u'>1',pos=u'050',desc=u'Additional Text'),
  Element( u'MSG01', Properties(desc=u'Free-Form Message Text', req_sit=u'R', data_type=(u'AN',u'1',u'264'), position=1,
    codes=[] ) ),
  Element( u'MSG02', Properties(desc=u'Printer Carriage Control Code', req_sit=u'N', data_type=(u'ID',u'2',u'2'), position=2,
    codes=[] ) ),
  Element( u'MSG03', Properties(desc=u'Number', req_sit=u'N', data_type=(u'N0',u'1',u'9'), position=3,
    codes=[] ) ),
),
)
parsed_841_2000 = Loop( u'2000', Properties(looptype='',repeat=u'>1',pos=u'010',req_sit=u'R',desc=u'Code List Header'), 
Segment( u'HL', Properties(syntax='',req_sit=u'R',repeat=u'1',pos=u'010',desc=u'Code List Header'),
  Element( u'HL01', Properties(desc=u'Hierarchical ID Number', req_sit=u'R', data_type=(u'AN',u'1',u'12'), position=1,
    codes=[u'1'] ) ),
  Element( u'HL02', Properties(desc=u'Hierarchical Parent ID Number', req_sit=u'N', data_type=(u'AN',u'1',u'12'), position=2,
    codes=[] ) ),
  Element( u'HL03', Properties(desc=u'Hierarchical Level Code', req_sit=u'R', data_type=(u'ID',u'1',u'2'), position=3,
    codes=[u'I'] ) ),
  Element( u'HL04', Properties(desc=u'Hierarchical Child Code', req_sit=u'N', data_type=(u'ID',u'1',u'1'), position=4,
    codes=[] ) ),
),
parsed_841_2100,
)
parsed_841_DETAIL = Loop( u'DETAIL', Properties(looptype=u'wrapper',repeat=u'>1',pos=u'020',req_sit=u'S',desc=u'Table 2 - Detail'), 
parsed_841_2000,
)
parsed_841_ST_LOOP = Loop( u'ST_LOOP', Properties(looptype=u'explicit',repeat=u'>1',pos=u'020',req_sit=u'R',desc=u'Transaction Set Header'), 
Segment( u'ST', Properties(syntax='',req_sit=u'R',repeat=u'1',pos=u'005',desc=u'Transaction Set Header'),
  Element( u'ST01', Properties(desc=u'Transaction Set Identifier Code', req_sit=u'R', data_type=(u'ID',u'3',u'3'), position=1,
    codes=[u'841'] ) ),
  Element( u'ST02', Properties(desc=u'Transaction Set Control Number', req_sit=u'R', data_type=(u'AN',u'4',u'9'), position=2,
    codes=[] ) ),
),
parsed_841_HEADER,
parsed_841_DETAIL,
Segment( u'SE', Properties(syntax='',req_sit=u'R',repeat=u'1',pos=u'210',desc=u'Transaction Set Trailer'),
  Element( u'SE01', Properties(desc=u'Number of Included Segments', req_sit=u'R', data_type=(u'N0',u'1',u'10'), position=1,
    codes=[] ) ),
  Element( u'SE02', Properties(desc=u'Transaction Set Control Number', req_sit=u'R', data_type=(u'AN',u'4',u'9'), position=2,
    codes=[] ) ),
),
)
parsed_841_GS_LOOP = Loop( u'GS_LOOP', Properties(looptype=u'explicit',repeat=u'>1',pos=u'020',req_sit=u'R',desc=u'Functional Group Header'), 
Segment( u'GS', Properties(syntax='',req_sit=u'R',repeat=u'1',pos=u'010',desc=u'Functional Group Header'),
  Element( u'GS01', Properties(desc=u'Functional Identifier Code', req_sit=u'R', data_type=(u'ID',u'2',u'2'), position=1,
    codes=[u'SP'] ) ),
  Element( u'GS02', Properties(desc=u'Application Senders Code', req_sit=u'R', data_type=(u'AN',u'2',u'15'), position=2,
    codes=[] ) ),
  Element( u'GS03', Properties(desc=u'124', req_sit=u'R', data_type=(u'AN',u'2',u'15'), position=3,
    codes=[] ) ),
  Element( u'GS04', Properties(desc=u'Date', req_sit=u'R', data_type=(u'DT',u'8',u'8'), position=4,
    codes=[] ) ),
  Element( u'GS05', Properties(desc=u'Time', req_sit=u'R', data_type=(u'TM',u'4',u'8'), position=5,
    codes=[] ) ),
  Element( u'GS06', Properties(desc=u'Group Control Number', req_sit=u'R', data_type=(u'N0',u'1',u'9'), position=6,
    codes=[] ) ),
  Element( u'GS07', Properties(desc=u'Responsible Agency Code', req_sit=u'R', data_type=(u'ID',u'1',u'2'), position=7,
    codes=[u'X'] ) ),
  Element( u'GS08', Properties(desc=u'Version / Release / Industry Identifier Code', req_sit=u'R', data_type=(u'AN',u'1',u'12'), position=8,
    codes=[u'004010XXXC'] ) ),
),
parsed_841_ST_LOOP,
Segment( u'GE', Properties(syntax='',req_sit=u'R',repeat=u'1',pos=u'030',desc=u'Functional Group Trailer'),
  Element( u'GE01', Properties(desc=u'97', req_sit=u'R', data_type=(u'N0',u'1',u'6'), position=1,
    codes=[] ) ),
  Element( u'GE02', Properties(desc=u'Group Control Number', req_sit=u'R', data_type=(u'N0',u'1',u'9'), position=2,
    codes=[] ) ),
),
)
parsed_841_ISA_LOOP = Loop( u'ISA_LOOP', Properties(looptype=u'explicit',repeat=u'>1',pos=u'001',req_sit=u'R',desc=u'Interchange Control Header'), 
Segment( u'ISA', Properties(syntax='',req_sit=u'R',repeat=u'1',pos=u'010',desc=u'Interchange Control Header'),
  Element( u'ISA01', Properties(desc=u'I01', req_sit=u'R', data_type=(u'ID',u'2',u'2'), position=1,
    codes=[u'00', u'03'] ) ),
  Element( u'ISA02', Properties(desc=u'I02', req_sit=u'R', data_type=(u'AN',u'10',u'10'), position=2,
    codes=[] ) ),
  Element( u'ISA03', Properties(desc=u'I03', req_sit=u'R', data_type=(u'ID',u'2',u'2'), position=3,
    codes=[u'00', u'01'] ) ),
  Element( u'ISA04', Properties(desc=u'I04', req_sit=u'R', data_type=(u'AN',u'10',u'10'), position=4,
    codes=[] ) ),
  Element( u'ISA05', Properties(desc=u'I05', req_sit=u'R', data_type=(u'ID',u'2',u'2'), position=5,
    codes=[u'01', u'14', u'20', u'27', u'28', u'29', u'30', u'33', u'ZZ'] ) ),
  Element( u'ISA06', Properties(desc=u'I06', req_sit=u'R', data_type=(u'AN',u'15',u'15'), position=6,
    codes=[] ) ),
  Element( u'ISA07', Properties(desc=u'I05', req_sit=u'R', data_type=(u'ID',u'2',u'2'), position=7,
    codes=[u'01', u'14', u'20', u'27', u'28', u'29', u'30', u'33', u'ZZ'] ) ),
  Element( u'ISA08', Properties(desc=u'I07', req_sit=u'R', data_type=(u'AN',u'15',u'15'), position=8,
    codes=[] ) ),
  Element( u'ISA09', Properties(desc=u'I08', req_sit=u'R', data_type=(u'DT',u'6',u'6'), position=9,
    codes=[] ) ),
  Element( u'ISA10', Properties(desc=u'I09', req_sit=u'R', data_type=(u'TM',u'4',u'4'), position=10,
    codes=[] ) ),
  Element( u'ISA11', Properties(desc=u'I10', req_sit=u'R', data_type=(u'ID',u'1',u'1'), position=11,
    codes=[u'U'] ) ),
  Element( u'ISA12', Properties(desc=u'I11', req_sit=u'R', data_type=(u'ID',u'5',u'5'), position=12,
    codes=[u'00401'] ) ),
  Element( u'ISA13', Properties(desc=u'I12', req_sit=u'R', data_type=(u'N0',u'9',u'9'), position=13,
    codes=[] ) ),
  Element( u'ISA14', Properties(desc=u'I13', req_sit=u'R', data_type=(u'ID',u'1',u'1'), position=14,
    codes=[u'0', u'1'] ) ),
  Element( u'ISA15', Properties(desc=u'I14', req_sit=u'R', data_type=(u'ID',u'1',u'1'), position=15,
    codes=[u'P', u'T'] ) ),
  Element( u'ISA16', Properties(desc=u'I15', req_sit=u'R', data_type=(u'AN',u'1',u'1'), position=16,
    codes=[] ) ),
),
parsed_841_GS_LOOP,
Segment( u'TA1', Properties(syntax='',req_sit=u'S',repeat=u'1',pos=u'020',desc=u'Interchange Acknowledgement'),
  Element( u'TA101', Properties(desc=u'I12', req_sit=u'R', data_type=(u'N0',u'9',u'9'), position=1,
    codes=[] ) ),
  Element( u'TA102', Properties(desc=u'I08', req_sit=u'R', data_type=(u'DT',u'6',u'6'), position=2,
    codes=[] ) ),
  Element( u'TA103', Properties(desc=u'I09', req_sit=u'R', data_type=(u'TM',u'4',u'4'), position=3,
    codes=[] ) ),
  Element( u'TA104', Properties(desc=u'I17', req_sit=u'R', data_type=(u'ID',u'1',u'1'), position=4,
    codes=[u'A', u'E', u'R'] ) ),
  Element( u'TA105', Properties(desc=u'I18', req_sit=u'R', data_type=(u'ID',u'3',u'3'), position=5,
    codes=[u'000', u'001', u'002', u'003', u'004', u'005', u'006', u'007', u'008', u'009', u'010', u'011', u'012', u'013', u'014', u'015', u'016', u'017', u'018', u'019', u'020', u'021', u'022', u'023', u'024', u'025', u'026', u'027', u'028', u'029', u'030', u'031'] ) ),
),
Segment( u'IEA', Properties(syntax='',req_sit=u'R',repeat=u'1',pos=u'030',desc=u'Interchange Control Trailer'),
  Element( u'IEA01', Properties(desc=u'I16', req_sit=u'R', data_type=(u'N0',u'1',u'5'), position=1,
    codes=[] ) ),
  Element( u'IEA02', Properties(desc=u'I12', req_sit=u'R', data_type=(u'N0',u'9',u'9'), position=2,
    codes=[] ) ),
),
)
parsed_841 = Message( u'841', Properties(desc=u'HIPAA Related Code Lists'), 
parsed_841_ISA_LOOP,
)
