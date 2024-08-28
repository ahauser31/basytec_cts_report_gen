#==============================================================================
# author 			: Andreas Hauser
# contact 			: andreas_hauser@artc.a-star.edu.sg
# title				: report_gen.py
# description		: Read Basytec CTS calibration data and generate a
#                     Calibration report in typst format
# date				: 17/08/2024
# version			: 1.0.0
# dependencies		: argparse, sys, os, datetime
# external deps     : colorful-terminal, pypxlib
# usage				: Run with -h parameter for help
# notes				: Quality = abs(error)/tolerance * 100
#==============================================================================

import sys
import os
import argparse
import datetime
# import csv
from colorful_terminal import colored_print, Fore, Style
from pypxlib import Table


###############################################################################
# Constants definitions
###############################################################################

VERSION = '1.0.0'
DEFAULT_CHANNELS = 32

SOP_NAME = 'Calibrating BaSyTec Battery Test System'
SOP_DATE = '5/6/2024'
SOFTWARE_VERSION = '6.0.16.0'


###############################################################################
# Class definitons
###############################################################################

class Settings:
    def __init__(self):
        self.template = None
        self.calData= None
        self.channelFile = None
        self.numChannels = DEFAULT_CHANNELS
        self.reportNumber = None
        self.verbose = False
        self.serialNumber = None
        self.deviceId = 0
        self.calDate = None
        self.recommendedNextCal = None
        self.receivedDate = None
        self.clientName = None
        self.clientAddress1 = None
        self.clientAddress2 = None
        self.clientAddress = None
        self.calByName = None
        self.calByTitle = None
        self.approvedByName = None
        self.approvedByTitle = None
        self.calDateMultimeter = None
        self.calReportMultimeter = None
        self.calDateCalibrator = None
        self.calReportCalibrator = None
        self.outputFile = None
    # end def

    def __str__(self):
        return (
            'CalData: ' + self.calData + '\n' + \
            'Template: ' + self.template + '\n' + \
            'Channel file: ' + self.channelFile + '\n' + \
            '------------------------\n' + \
            'Serial number: ' + self.serialNumber + '\n' + \
            'Device ID: ' + str(self.deviceId) + '\n' + \
            'Number of channels: ' + str(self.numChannels) + '\n' + \
            'Received date: ' + self.receivedDate.strftime('%d/%m/%Y') + '\n' + \
            'Calibration date: ' + self.calDate.strftime('%d/%m/%Y') + '\n' + \
            'Calibration due date: ' + self.recommendedNextCal.strftime('%d/%m/%Y') + '\n' + \
            '------------------------\n' + \
            'Client name: ' + self.clientName + '\n' + \
            'Client address 1: ' + self.clientAddress1 + '\n' + \
            'Client address 2: ' + self.clientAddress2 + '\n' + \
            'Client address 3: ' + self.clientAddress3 + '\n' + \
            '------------------------\n' + \
            'Report number: ' + self.reportNumber + '\n' + \
            'Calibration by: ' + self.calByName + '\n' + \
            'Calibration by (title): ' + self.calByTitle + '\n' + \
            'Approved by: ' + self.approvedByName + '\n' + \
            'Approved by (title): ' + self.approvedByTitle + '\n' + \
            'Output file: ' + self.outputFile + '\n' + \
            '------------------------\n' + \
            'Date calibration Multimeter: ' + self.calDateMultimeter.strftime('%d/%m/%Y') + '\n' + \
            'Calibration report number Multimeter: ' + self.calReportMultimeter + '\n' + \
            'Date calibration Calibrator: ' + self.calDateCalibrator.strftime('%d/%m/%Y') + '\n' + \
            'Calibration report number Calibrator: ' + self.calReportCalibrator + '\n' + \
            '------------------------\n' + \
            'Verbose: ' + ('TRUE' if self.verbose else 'FALSE'))
    # end def

    def fromCommandLine(self, commandLineArgs):
        self.calData = commandLineArgs.caldata
        self.template = commandLineArgs.template
        self.channelFile = commandLineArgs.channelfile
        if commandLineArgs.numchannels > 0:
            self.numChannels = commandLineArgs.numchannels
        # end if
        self.verbose = commandLineArgs.verbose
    # end def

    def getSerial(self):
        self.serialNumber = input('Enter serial number: ')
        if self.serialNumber == '' or self.serialNumber is None:
            raise ValueError('Serial number cannot be empty')
        # end if

        # Get device ID from serial number
        tmp = self.serialNumber[self.serialNumber.rindex('.') + 1:]
        self.deviceId = int(tmp)
    # end def

    def getCalDate(self):
        calDateRaw = input('Enter calibration date (dd/mm/yyyy): ')
        tmpDate = calDateRaw.split('/')
        self.calDate = datetime.date(int(tmpDate[2]), int(tmpDate[1]), int(tmpDate[0]))
        self.recommendedNextCal = self.calDate + datetime.timedelta(days=365)
    # end def

    def getReceivedDate(self):
        recvDateRaw = input('Enter received date (dd/mm/yyyy): ')
        tmpDate = recvDateRaw.split('/')
        self.receivedDate = datetime.date(int(tmpDate[2]), int(tmpDate[1]), int(tmpDate[0]))
    # end def

    def getClientDetails(self):
        self.clientName = input('Enter client name: ')
        self.clientAddress1 = input('Enter client address line 1: ')
        self.clientAddress2 = input('Enter client address line 2: ')
        self.clientAddress3 = input('Enter client address line 3: ')
    # end def

    def getCalStaff(self):
        self.calByName = input('Enter name of calibration operator: ')
        self.calByTitle = input('Enter title of calibration operator: ')
        self.approvedByName = input('Enter name of calibration approver: ')
        self.approvedByTitle = input('Enter title of calibration approver: ')
    # end def

    def getCalEquipment(self):
        calDateMultimeter = input('Enter calibration due date of Multimeter HM 8112-3 (dd/mm/yyy): ')
        tmpDate = calDateMultimeter.split('/')
        self.calDateMultimeter = datetime.date(int(tmpDate[2]), int(tmpDate[1]), int(tmpDate[0]))
        self.calReportMultimeter = input('Enter calibration report number of Multimeter HM 8112-3: ')

        calDateCalibrator = input('Enter calibration due date of CTS calibration device (dd/mm/yyy): ')
        tmpDate = calDateCalibrator.split('/')
        self.calDateCalibrator = datetime.date(int(tmpDate[2]), int(tmpDate[1]), int(tmpDate[0]))
        self.calReportCalibrator = input('Enter calibration report number of CTS calibration device: ')
    # end def

    def getReportNumber(self):
        self.reportNumber = input('Enter report number: ')
    # end def

    def setOutputFile(self):
        self.outputFile = os.path.join(os.path.dirname(sys.argv[0]), 'Calibration Report ' + self.serialNumber + ' - Report number ' + self.reportNumber + '.typ')
        # file = open(settings.output, 'w', encoding='utf-8', newline='')
    # end def

# end class


class CTS:
    def __init__(self, settings):
        self.numChannels = settings.numChannels
        self.channels = {}
        self.deviceId = settings.deviceId
        self.calDate = settings.calDate

        self.calData =  Table(settings.calData, px_encoding='cp1252')
        self.channelFile =  Table(settings.channelFile, px_encoding='cp1252')
    # end def

    def __del__(self):
        self.calData.close()
        self.channelFile.close()
    # end def

    def __str__(self):
        res = 'Num. channels: ' + str(len(self.channels)) + '\n'
        if len(self.channels) > 0:
            for key, value in self.channels.items():
                res = res + 'Channel: ' + str(key) + '\n' + str(value) + '\n' + '------------------------' + '\n'
            # end for
        # end if
        return res
    # end def

    def readChannel(self, channelNumber):
        # Define channel ID to search for
        channelId = str(self.deviceId) + ' CH' + ('' if channelNumber > 9 else '0') +  str(channelNumber) + ' CTS'
        channel = CTSChannel(channelNumber)

        # Determine range based on channel number
        if channelNumber % 2 == 0:
            # First channel has a range from 1 to 21
            rangeFrom = 1
            rangeTo = 22
        else:
            # Second channel has a range from 22 to 42
            rangeFrom = 22
            rangeTo = 43
        # end if

        # Read caldata
        priorRow = 0
        for entryNumber in range(rangeFrom, rangeTo):
            # Trick to speed up search (early abort of record search when both post and pre measurement are found)
            countFound = 0

            for rowNumber in range(priorRow, len(self.calData)):
                tableRow = self.calData[rowNumber]
                if (tableRow['Date'].year == self.calDate.year and tableRow['Date'].month == self.calDate.month and tableRow['Date'].day == self.calDate.day and tableRow['Channel_Id'] == channelId and tableRow['No'] == entryNumber):
                    # Found either the post- or pre measurement for that range
                    preMeasurement = False
                    countFound = countFound + 1

                    # Save number of the row, so search does not have to start from scratch
                    priorRow = rowNumber

                    # Determine if this is the pre- or post measurement
                    if tableRow['Range'].startswith('PRE'):
                        preMeasurement = True
                    # end if

                    # Store record
                    channel.addRecord((entryNumber if entryNumber < 22 else entryNumber - 21), preMeasurement, tableRow['Ref_value'], tableRow['Meas_value'], tableRow['Error'], tableRow['Tolerance'])
                    if abs(tableRow['Error']) > tableRow['Tolerance']:
                        # Channel out of spec
                        channel.setOufOfSpec(preMeasurement, (entryNumber if entryNumber < 22 else entryNumber - 21))
                    # end if

                    if countFound == 2:
                        break
                    # end if
                # end if
            # end for
        # end for

        # Read channelfile
        for tableRow in self.channelFile:
            if tableRow['Id'] == channelId:
                # Found correct record, save out params
                i1Factors = {'factor': tableRow['Fak0'], 'offset': tableRow['Off0']}
                i2Factors = {'factor': tableRow['Fak4'], 'offset': tableRow['Off4']}
                i3Factors = {'factor': tableRow['Fak5'], 'offset': tableRow['Off5']}
                i4Factors = {'factor': tableRow['Fak2'], 'offset': tableRow['Off2']}
                uFactors = {'factor': tableRow['Fak1'], 'offset': tableRow['Off1']}
                tFactors = {'factor': tableRow['Fak3'], 'offset': tableRow['Off3']}
                channel.setFactors(i1Factors, i2Factors, i3Factors, i4Factors, uFactors, tFactors)
        # end for

        # Save extracted data
        self.channels[channelNumber] = channel
    # end def

# end class


class CTSChannel:
    def __init__(self, channelNumber):
        self.channelNumber = channelNumber
        self.records = {}
        self.factors = {}
        self.preOutOfSpec = set()
        self.postOutOfSpec = set()
    # end def

    def __str__(self):
        res = ''
        if len(self.records) > 0:
            for key, value in self.records.items():
                res = res + str(key) +  ' -> ' +  str(value) + '\n'
            # end for
        # end if

        for key, factor in self.factors:
            res = res + 'Value: ' + key + ' - Range: ' + factor['range'] + ' - Factor: ' + str(factor['factor']) + ' - Offset: ' + str(factor['offset']) + '\n'
        # end for
        if len(self.factors) == 0:
            res = res + 'No calibration factors found for channel!\n'
        # end if

        res = res + 'Channel out of spec. prior to Calibration: ' + ('YES' if len(self.preOutOfSpec) > 0 else 'NO') + ('(' + str(self.preOutOfSpec) + ')' if len(self.preOutOfSpec) > 0 else '') + '\n'
        res = res + 'Channel out of spec. post Calibration: ' + ('YES' if len(self.postOutOfSpec) > 0 else 'NO') + ('(' + str(self.postOutOfSpec) + ')' if len(self.postOutOfSpec) > 0 else '') + '\n'

        return res
    # end def

    def setOufOfSpec(self, preMeasurement, entryNumber):
        # Determine range that is problematic
        rangeOOS = ''
        if entryNumber >= 1 and entryNumber <= 4:
            rangeOOS = '1 mA'
        elif entryNumber >= 5 and entryNumber <= 8:
            rangeOOS = '15 mA'
        elif entryNumber >= 9 and entryNumber <= 12:
            rangeOOS = '300 mA'
        elif entryNumber >= 13 and entryNumber <= 16:
            rangeOOS = '5 A'
        elif entryNumber >= 17 and entryNumber <= 19:
            rangeOOS = '6 V'
        elif entryNumber == 20 or entryNumber == 21:
            rangeOOS = 'T1'
        # end if

        if preMeasurement:
            self.preOutOfSpec.add(rangeOOS)
        else:
            self.postOutOfSpec.add(rangeOOS)
    # end def

    def addRecord(self, rangeValue, preMeasurement, refValue, measValue, error, tolerance):
        if preMeasurement:
            rangeValue = rangeValue + 100
        # end if

        self.records[rangeValue] = CalRecord(refValue, measValue, error, tolerance, None)
    # end def

    def setFactors(self, i1Factors, i2Factors, i3Factors, i4Factors, uFactors, tFactors):
        i1Factors['range'] = '±1 mA'
        i2Factors['range'] = '±15 mA'
        i3Factors['range'] = '±300 mA'
        i4Factors['range'] = '±5 A'
        uFactors['range'] = '0 - 6 V'
        tFactors['range'] = '-30°C to 100°C'

        self.factors['I1'] = i1Factors
        self.factors['I2'] = i2Factors
        self.factors['I3'] = i3Factors
        self.factors['I4'] = i4Factors
        self.factors['U'] = uFactors
        self.factors['T'] = tFactors
    # end def
# end class


class CalRecord:
    def __init__(self, refValue, measValue, error, tolerance, uncertainty):
        self.refValue = refValue if refValue is not None else 0.0
        self.measValue = measValue if measValue is not None else 0.0
        self.error = error if error is not None else 0.0
        self.tolerance = tolerance if tolerance is not None else 0.0
        self.uncertainty = uncertainty if uncertainty is not None else 0.0
    # end def

    def __str__(self):
        return 'Ref: ' + str(self.refValue) + ' Meas: ' + str(self.measValue) + ' Error: ' + str(self.error) + ' Tolerance: ' + str(self.tolerance) + ' Uncertainty: ' + str(self.uncertainty)
    # end def
# end class


###############################################################################
# Settings
###############################################################################

def readCommandLineArgs():
    '''
    Read command line parameters
    '''
    parser = argparse.ArgumentParser(description='Read BaSyTec CTS calibration data and create report in typst format - Ver.: ' + VERSION)
    parser.add_argument('-d',
                        '--caldata',
                        required=True,
                        help='Caldata file [caldata.db]')
    parser.add_argument('-c',
                        '--channelfile',
                        required=True,
                        help='Channel file [channel.db]')
    parser.add_argument('-n',
                        '--numchannels',
                        required=False,
                        type=int,
                        default=DEFAULT_CHANNELS,
                        help='Number of test in tests.db [optional parameter, either test number or test name need to be specified]')
    parser.add_argument('-t',
                        '--template',
                        required=True,
                        help='Template for calibration report [*.typst]')
    parser.add_argument('-v',
                        '--verbose',
                        required=False,
                        action='store_true',
                        help='Show more messages during processing (Default: false)')

    return parser.parse_args()
# end def

def initAndLoadSettings():
    settings = Settings()

    try:
        settings.fromCommandLine(readCommandLineArgs())
        if not os.path.isfile(settings.channelFile):
            raise ValueError('File not found: ' + settings.channelFile)
        if not os.path.isfile(settings.calData):
            raise ValueError('File not found: ' + settings.calData)
        if not os.path.isfile(settings.template):
            raise ValueError('File not found: ' + settings.template)

        # Get additional settings from user
        colored_print(Fore.BLUE + '\n-- Basytec report generator --')
        settings.getReportNumber()
        settings.getSerial()
        settings.getReceivedDate()
        settings.getCalDate()
        settings.getClientDetails()
        settings.getCalStaff()
        settings.getCalEquipment()
        settings.setOutputFile()
    except Exception as error:
        colored_print(Fore.RED + 'ERROR: ' + error.args[0])
        sys.exit(1)
    # end exception

    if settings.verbose:
        colored_print(Fore.BLUE + '\n\nSettings:')
        print(settings)
    # end if

    return settings
# end def


###############################################################################
# Reading calibration data
###############################################################################

def printProgressBar(percentage, label, reset):
    if percentage < 0:
        percentage = 0
    elif percentage > 100:
        percentage = 100
    # end if

    numFullBlocks = int(percentage / 8)
    partialBlock = percentage % 8
    indicator = ['█'] * numFullBlocks
    if partialBlock == 1:
        indicator.append('▏')
    elif partialBlock == 2:
        indicator.append('▎')
    elif partialBlock == 3:
        indicator.append('▍')
    elif partialBlock == 4:
        indicator.append('▌')
    elif partialBlock == 5:
        indicator.append('▋')
    elif partialBlock == 6:
        indicator.append('▊')
    elif partialBlock == 7:
        indicator.append('▉')
    # end if
    indicatorString = ''.join(indicator)
    print(Fore.BLUE + label + '  ' + str(percentage) + '%  ' + Style.RESET_ALL + Fore.GREEN + indicatorString + Style.RESET_ALL, end= ('\r' if not reset else '\n'))
# end def

def readCalibrationData(settings, cts):
    # cts.readChannel(0)
    # return

    # Prepare progress bar
    progress = 0.0
    pInc = 100 / settings.numChannels
    progressLabel = 'Reading caldata.DB and channel.DB...'
    print('\n\n')
    printProgressBar(int(progress), progressLabel, False)

    for channel in range(0, settings.numChannels):
        cts.readChannel(channel)
        progress = progress + pInc
        printProgressBar(int(progress), progressLabel, False)
    # end for

    # Print final progress bar
    printProgressBar(int(progress), progressLabel, True)
# end def


###############################################################################
# Writing output file
###############################################################################

def sanitizeTypst(string):
    # Escape typst control characters
    res = string.replace('#', '\\#')
    res = res.replace('@', '\\@')
    res = res.replace('$', '\\$')
    return res
# end def

def readTemplate(settings):
    f = open(settings.template, 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()

    return lines
# end def

def writeParameters(settings, cts, f):    
    f.write('#let signer_name = [' + sanitizeTypst(settings.approvedByName) + ']\n')
    f.write('#let signer_title = [' + sanitizeTypst(settings.approvedByTitle) + ']\n')

    f.write('#let calibrated_by = [' + sanitizeTypst(settings.calByName) + ']\n')
    f.write('#let calibrated_by_title = [' + sanitizeTypst(settings.calByTitle) + ']\n')

    f.write('#let report_number = [' + sanitizeTypst(settings.reportNumber) + ']\n')

    f.write('#let submitter_company = [' + sanitizeTypst(settings.clientName) + ']\n')
    f.write('#let submitter_company_address = [' + sanitizeTypst(settings.clientAddress1) + '\\ ' + sanitizeTypst(settings.clientAddress2) + '\\ ' + sanitizeTypst(settings.clientAddress3) + ']\n')

    f.write('#let tester_model = [CTS ' + str(settings.numChannels) + ' channel]\n')
    f.write('#let tester_serial = [' + settings.serialNumber + ']\n')
    f.write('#let tester_id = [' + str(settings.deviceId) + ']\n')

    f.write('#let date_received = [' + settings.receivedDate.strftime('%d/%m/%Y') + ']\n')
    f.write('#let date_calibrated = [' + settings.calDate.strftime('%d/%m/%Y') + ']\n')
    f.write('#let date_recommended = [' + settings.recommendedNextCal.strftime('%d/%m/%Y') + ']\n')

    f.write('#let calibration_sop = [' + sanitizeTypst(SOP_NAME) + ']\n')
    f.write('#let calibration_sop_date = [' + sanitizeTypst(SOP_DATE) + ']\n')
    f.write('#let software_version = [' + sanitizeTypst(SOFTWARE_VERSION) + ']\n')

    f.write('#let multimeter_due = [' + settings.calDateMultimeter.strftime('%d/%m/%Y') + ']\n')
    f.write('#let multimeter_report = [' + sanitizeTypst(settings.calReportMultimeter) + ']\n')
    f.write('#let calibrator_due = [' + settings.calDateCalibrator.strftime('%d/%m/%Y') + ']\n')
    f.write('#let calibrator_report = [' + sanitizeTypst(settings.calReportCalibrator) + ']\n')

    # Determine if any parameter was out of specification
    preOutOfSpec = ''
    postOutOfSpec = ''
    for key, channel in cts.channels.items():
        if len(channel.preOutOfSpec) > 0:
            preOutOfSpecRange = None
            if len(preOutOfSpec) > 0:
                preOutOfSpec = preOutOfSpec + '; '
            # end if
            for rangeOOS in channel.preOutOfSpec:
                preOutOfSpecRange = (preOutOfSpecRange + '; ' + rangeOOS if preOutOfSpecRange is not None else rangeOOS) 
            # end for
            preOutOfSpec = preOutOfSpec + 'CH' + ('0' if channel.channelNumber < 10 else '') + str(channel.channelNumber) + ' (' + preOutOfSpecRange + ')'
        # end if

        if len(channel.postOutOfSpec) > 0:
            postOutOfSpecRange = None
            if len(postOutOfSpec) > 0:
                postOutOfSpec = postOutOfSpec + '; '
            # end if
            for rangeOOS in channel.postOutOfSpec:
                postOutOfSpecRange = (postOutOfSpecRange + '; ' + rangeOOS if postOutOfSpecRange is not None else rangeOOS) 
            # end for
            postOutOfSpec = postOutOfSpec + 'CH' + ('0' if channel.channelNumber < 10 else '') + str(channel.channelNumber) + ' (' + postOutOfSpecRange + ')'
        # end if
    # end for
    f.write('#let condition_received_tolerance = [' + ('YES' if len(preOutOfSpec) == 0 else 'NO') + ']\n')
    f.write('#let condition_received_remark = [' + ('N/A' if len(preOutOfSpec) == 0 else preOutOfSpec ) +']\n')
    f.write('#let condition_shipped_tolerance = [' + ('YES' if len(postOutOfSpec) == 0 else 'NO') + ']\n')
    f.write('#let condition_shipped_remark = [' + ('N/A' if len(postOutOfSpec) == 0 else postOutOfSpec ) +']\n')
    f.write('\n')
# end def

def writeChannelArrays(settings, cts, f):
    for key, channel in cts.channels.items():
        f.write('#let array' + str(channel.channelNumber) + ' = (\n')

        # I1
        formatter = '"{:7.6f} mA",\n'
        deviation = '"{:.4e} mA",\n'
        f.write(formatter.format(channel.records[101].refValue))   # "af I1 -90 av", 
        f.write(formatter.format(channel.records[101].measValue))  # "af I1 -90 mv",
        f.write(deviation.format(channel.records[101].error))      # "af I1 -90 dv",
        f.write(formatter.format(channel.records[1].refValue))     # "al I1 -90 av",
        f.write(formatter.format(channel.records[1].measValue))    # "al I1 -90 mv",
        f.write(deviation.format(channel.records[1].error))        # "al I1 -90 dv",
        f.write(formatter.format(channel.records[1].uncertainty))  # "I1 -90 uc",

        f.write(formatter.format(channel.records[102].refValue))   # "af I1 -10 av", 
        f.write(formatter.format(channel.records[102].measValue))  # "af I1 -10 mv",
        f.write(deviation.format(channel.records[102].error))      # "af I1 -10 dv",
        f.write(formatter.format(channel.records[2].refValue))     # "al I1 -10 av",
        f.write(formatter.format(channel.records[2].measValue))    # "al I1 -10 mv",
        f.write(deviation.format(channel.records[2].error))        # "al I1 -10 dv",
        f.write(formatter.format(channel.records[2].uncertainty))  # "I1 -10 uc",

        f.write(formatter.format(channel.records[103].refValue))   # "af I1 10 av", 
        f.write(formatter.format(channel.records[103].measValue))  # "af I1 10 mv",
        f.write(deviation.format(channel.records[103].error))      # "af I1 10 dv",
        f.write(formatter.format(channel.records[3].refValue))     # "al I1 10 av",
        f.write(formatter.format(channel.records[3].measValue))    # "al I1 10 mv",
        f.write(deviation.format(channel.records[3].error))        # "al I1 10 dv",
        f.write(formatter.format(channel.records[3].uncertainty))  # "I1 10 uc",

        f.write(formatter.format(channel.records[104].refValue))   # "af I1 90 av", 
        f.write(formatter.format(channel.records[104].measValue))  # "af I1 90 mv",
        f.write(deviation.format(channel.records[104].error))      # "af I1 90 dv",
        f.write(formatter.format(channel.records[4].refValue))     # "al I1 90 av",
        f.write(formatter.format(channel.records[4].measValue))    # "al I1 90 mv",
        f.write(deviation.format(channel.records[4].error))        # "al I1 90 dv",
        f.write(formatter.format(channel.records[4].uncertainty))  # "I1 90 uc",

        # I2
        formatter = '"{:7.5f} mA",\n'
        deviation = '"{:.4e} mA",\n'
        f.write(formatter.format(channel.records[105].refValue))   # "af I2 -90 av", 
        f.write(formatter.format(channel.records[105].measValue))  # "af I2 -90 mv",
        f.write(deviation.format(channel.records[105].error))      # "af I2 -90 dv",
        f.write(formatter.format(channel.records[5].refValue))     # "al I2 -90 av",
        f.write(formatter.format(channel.records[5].measValue))    # "al I2 -90 mv",
        f.write(deviation.format(channel.records[5].error))        # "al I2 -90 dv",
        f.write(formatter.format(channel.records[5].uncertainty))  # "I2 -90 uc",

        formatter = '"{:7.6f} mA",\n'
        f.write(formatter.format(channel.records[106].refValue))   # "af I2 -10 av", 
        f.write(formatter.format(channel.records[106].measValue))  # "af I2 -10 mv",
        f.write(deviation.format(channel.records[106].error))      # "af I2 -10 dv",
        f.write(formatter.format(channel.records[6].refValue))     # "al I2 -10 av",
        f.write(formatter.format(channel.records[6].measValue))    # "al I2 -10 mv",
        f.write(deviation.format(channel.records[6].error))        # "al I2 -10 dv",
        f.write(formatter.format(channel.records[6].uncertainty))  # "I2 -10 uc",

        f.write(formatter.format(channel.records[107].refValue))   # "af I2 10 av", 
        f.write(formatter.format(channel.records[107].measValue))  # "af I2 10 mv",
        f.write(deviation.format(channel.records[107].error))      # "af I2 10 dv",
        f.write(formatter.format(channel.records[7].refValue))     # "al I2 10 av",
        f.write(formatter.format(channel.records[7].measValue))    # "al I2 10 mv",
        f.write(deviation.format(channel.records[7].error))        # "al I2 10 dv",
        f.write(formatter.format(channel.records[7].uncertainty))  # "I2 10 uc",

        formatter = '"{:7.5f} mA",\n'
        f.write(formatter.format(channel.records[108].refValue))   # "af I2 90 av", 
        f.write(formatter.format(channel.records[108].measValue))  # "af I2 90 mv",
        f.write(deviation.format(channel.records[108].error))      # "af I2 90 dv",
        f.write(formatter.format(channel.records[8].refValue))     # "al I2 90 av",
        f.write(formatter.format(channel.records[8].measValue))    # "al I2 90 mv",
        f.write(deviation.format(channel.records[8].error))        # "al I2 90 dv",
        f.write(formatter.format(channel.records[8].uncertainty))  # "I2 90 uc",

        # I3
        formatter = '"{:7.6f} A",\n'
        deviation = '"{:.4e} A",\n'
        f.write(formatter.format(channel.records[109].refValue))   # "af I3 -90 av", 
        f.write(formatter.format(channel.records[109].measValue))  # "af I3 -90 mv",
        f.write(deviation.format(channel.records[109].error))      # "af I3 -90 dv",
        f.write(formatter.format(channel.records[9].refValue))     # "al I3 -90 av",
        f.write(formatter.format(channel.records[9].measValue))    # "al I3 -90 mv",
        f.write(deviation.format(channel.records[9].error))        # "al I3 -90 dv",
        f.write(formatter.format(channel.records[9].uncertainty))  # "I3 -90 uc",

        formatter = '"{:7.5f} mA",\n'
        deviation = '"{:.4e} mA",\n'
        f.write(formatter.format(channel.records[110].refValue))   # "af I3 -10 av", 
        f.write(formatter.format(channel.records[110].measValue))  # "af I3 -10 mv",
        f.write(deviation.format(channel.records[110].error))      # "af I3 -10 dv",
        f.write(formatter.format(channel.records[10].refValue))     # "al I3 -10 av",
        f.write(formatter.format(channel.records[10].measValue))    # "al I3 -10 mv",
        f.write(deviation.format(channel.records[10].error))        # "al I3 -10 dv",
        f.write(formatter.format(channel.records[10].uncertainty))  # "I3 -10 uc",

        f.write(formatter.format(channel.records[111].refValue))   # "af I3 10 av", 
        f.write(formatter.format(channel.records[111].measValue))  # "af I3 10 mv",
        f.write(deviation.format(channel.records[111].error))      # "af I3 10 dv",
        f.write(formatter.format(channel.records[11].refValue))     # "al I3 10 av",
        f.write(formatter.format(channel.records[11].measValue))    # "al I3 10 mv",
        f.write(deviation.format(channel.records[11].error))        # "al I3 10 dv",
        f.write(formatter.format(channel.records[11].uncertainty))  # "I3 10 uc",

        formatter = '"{:7.6f} A",\n'
        deviation = '"{:.4e} A",\n'
        f.write(formatter.format(channel.records[112].refValue))   # "af I3 90 av", 
        f.write(formatter.format(channel.records[112].measValue))  # "af I3 90 mv",
        f.write(deviation.format(channel.records[112].error))      # "af I3 90 dv",
        f.write(formatter.format(channel.records[12].refValue))     # "al I3 90 av",
        f.write(formatter.format(channel.records[12].measValue))    # "al I3 90 mv",
        f.write(deviation.format(channel.records[12].error))        # "al I3 90 dv",
        f.write(formatter.format(channel.records[12].uncertainty))  # "I3 90 uc",

        # I4
        formatter = '"{:7.6f} A",\n'
        deviation = '"{:.4e} A",\n'
        f.write(formatter.format(channel.records[113].refValue))   # "af I4 -90 av", 
        f.write(formatter.format(channel.records[113].measValue))  # "af I4 -90 mv",
        f.write(deviation.format(channel.records[113].error))      # "af I4 -90 dv",
        f.write(formatter.format(channel.records[13].refValue))     # "al I4 -90 av",
        f.write(formatter.format(channel.records[13].measValue))    # "al I4 -90 mv",
        f.write(deviation.format(channel.records[13].error))        # "al I4 -90 dv",
        f.write(formatter.format(channel.records[13].uncertainty))  # "I4 -90 uc",

        f.write(formatter.format(channel.records[114].refValue))   # "af I4 -10 av", 
        f.write(formatter.format(channel.records[114].measValue))  # "af I4 -10 mv",
        f.write(deviation.format(channel.records[114].error))      # "af I4 -10 dv",
        f.write(formatter.format(channel.records[14].refValue))     # "al I4 -10 av",
        f.write(formatter.format(channel.records[14].measValue))    # "al I4 -10 mv",
        f.write(deviation.format(channel.records[14].error))        # "al I4 -10 dv",
        f.write(formatter.format(channel.records[14].uncertainty))  # "I4 -10 uc",

        f.write(formatter.format(channel.records[115].refValue))   # "af I4 10 av", 
        f.write(formatter.format(channel.records[115].measValue))  # "af I4 10 mv",
        f.write(deviation.format(channel.records[115].error))      # "af I4 10 dv",
        f.write(formatter.format(channel.records[15].refValue))     # "al I4 10 av",
        f.write(formatter.format(channel.records[15].measValue))    # "al I4 10 mv",
        f.write(deviation.format(channel.records[15].error))        # "al I4 10 dv",
        f.write(formatter.format(channel.records[15].uncertainty))  # "I4 10 uc",

        f.write(formatter.format(channel.records[116].refValue))   # "af I4 90 av", 
        f.write(formatter.format(channel.records[116].measValue))  # "af I4 90 mv",
        f.write(deviation.format(channel.records[116].error))      # "af I4 90 dv",
        f.write(formatter.format(channel.records[16].refValue))     # "al I4 90 av",
        f.write(formatter.format(channel.records[16].measValue))    # "al I4 90 mv",
        f.write(deviation.format(channel.records[16].error))        # "al I4 90 dv",
        f.write(formatter.format(channel.records[16].uncertainty))  # "I4 90 uc",

        # U
        formatter = '"{:7.6f} V",\n'
        deviation = '"{:.4e} V",\n'
        f.write(formatter.format(channel.records[117].refValue))   # "af U 10 av", 
        f.write(formatter.format(channel.records[117].measValue))  # "af U 10 mv",
        f.write(deviation.format(channel.records[117].error))      # "af U 10 dv",
        f.write(formatter.format(channel.records[17].refValue))     # "al U 10 av",
        f.write(formatter.format(channel.records[17].measValue))    # "al U 10 mv",
        f.write(deviation.format(channel.records[17].error))        # "al U 10 dv",
        f.write(formatter.format(channel.records[17].uncertainty))  # "U 10 uc",

        f.write(formatter.format(channel.records[118].refValue))   # "af U 50 av", 
        f.write(formatter.format(channel.records[118].measValue))  # "af U 50 mv",
        f.write(deviation.format(channel.records[118].error))      # "af U 50 dv",
        f.write(formatter.format(channel.records[18].refValue))     # "al U 50 av",
        f.write(formatter.format(channel.records[18].measValue))    # "al U 50 mv",
        f.write(deviation.format(channel.records[18].error))        # "al U 50 dv",
        f.write(formatter.format(channel.records[18].uncertainty))  # "U 50 uc",

        f.write(formatter.format(channel.records[119].refValue))   # "af U 90 av", 
        f.write(formatter.format(channel.records[119].measValue))  # "af U 90 mv",
        f.write(deviation.format(channel.records[119].error))      # "af U 90 dv",
        f.write(formatter.format(channel.records[19].refValue))     # "al U 90 av",
        f.write(formatter.format(channel.records[19].measValue))    # "al U 90 mv",
        f.write(deviation.format(channel.records[19].error))        # "al U 90 dv",
        f.write(formatter.format(channel.records[19].uncertainty))  # "U 90 uc",

        # T
        formatter = '"{:5.3f} °C",\n'
        f.write(formatter.format(channel.records[120].refValue))   # "af T r1 av", 
        f.write(formatter.format(channel.records[120].measValue))  # "af T r1 mv",
        f.write(deviation.format(channel.records[120].error))      # "af T r1 dv",
        f.write(formatter.format(channel.records[20].refValue))     # "al T r1 av",
        f.write(formatter.format(channel.records[20].measValue))    # "al T r1 mv",
        f.write(formatter.format(channel.records[20].error))        # "al T r1 dv",
        f.write(formatter.format(channel.records[20].uncertainty))  # "T r1 uc",

        f.write(formatter.format(channel.records[121].refValue))   # "af T r2 av", 
        f.write(formatter.format(channel.records[121].measValue))  # "af T r2 mv",
        f.write(deviation.format(channel.records[121].error))      # "af T r2 dv",
        f.write(formatter.format(channel.records[21].refValue))     # "al T r2 av",
        f.write(formatter.format(channel.records[21].measValue))    # "al T r2 mv",
        f.write(formatter.format(channel.records[21].error))        # "al T r2 dv",
        f.write(formatter.format(channel.records[21].uncertainty))  # "T r2 uc",

        # Factors
        formatter = '"{:19.18f}"'
        f.write(formatter.format(channel.factors['I1']['factor']) + ', ' + formatter.format(channel.factors['I1']['offset']) + ',\n')   # "I1 factor", "I1 offset", 
        f.write(formatter.format(channel.factors['I2']['factor']) + ', ' + formatter.format(channel.factors['I2']['offset']) + ',\n')   # "I1 factor", "I1 offset", 
        f.write(formatter.format(channel.factors['I3']['factor']) + ', ' + formatter.format(channel.factors['I3']['offset']) + ',\n')   # "I1 factor", "I1 offset", 
        f.write(formatter.format(channel.factors['I4']['factor']) + ', ' + formatter.format(channel.factors['I4']['offset']) + ',\n')   # "I1 factor", "I1 offset", 
        f.write(formatter.format(channel.factors['U']['factor']) + ', ' + formatter.format(channel.factors['U']['offset']) + ',\n')     # "U factor", "U offset", 
        formatter = '"{:6.5f}"'
        f.write(formatter.format(channel.factors['T']['factor']) + ', ' + formatter.format(channel.factors['T']['offset']) + ',\n')     # "T factor", "T offset", 

        f.write(')\n\n')
    # end for
# end def


def writeChannelFunctions(cts, f):
    for key, channel in cts.channels.items():
        f.write('#makechannel(' + str(channel.channelNumber) + ', array' + str(channel.channelNumber) + (', lastChannel: true' if cts.numChannels == (channel.channelNumber + 1) else '')+ ')\n')
    # end for
# end def

def writeData(settings, cts, template):
    f = open(settings.outputFile, 'w', encoding='utf-8')

    # Write parameters into output file
    writeParameters(settings, cts, f)

    # Write channel data into output file
    writeChannelArrays(settings, cts, f)

    # Write the actual template into the output file
    for line in template:
        f.write(line)
    # end for

    # Write the function calls to create the channel table at the end of the template
    writeChannelFunctions(cts, f)

    f.close()
# end def

###############################################################################
# Main
###############################################################################

def main():
    # Read application settings
    settings = initAndLoadSettings()

    # Create data storage and read calibration data
    cts = CTS(settings)
    readCalibrationData(settings, cts)

    # Read Typst template and write data out
    template = readTemplate(settings)
    writeData(settings, cts, template)

    colored_print(Fore.GREEN + '\nReport "' + settings.outputFile + '" created sucessfully!')

    # print('')
    # print(cts)
#end def


###############################################################################
# Script entry point
###############################################################################

# Only execute main function in main process (not in spawned threads)
if __name__ == '__main__':
    main()
    sys.exit(0)
# end if
