from selfdrive.car import dbc_dict

class CAR:
  IMPREZA = "2011 Mercedes E350"

FINGERPRINTS = {
  CAR.IMPREZA: [{
    1: 8, 2: 5, 3: 8, 4: 5, 5: 8, 14: 8, 21: 4, 69: 8, 95: 8, 105: 2, 109: 4, 115: 8, 213: 8, 222: 8, 243: 8, 249: 8, 254: 8, 255: 8, 257: 8, 260: 8, 261: 8, 301: 8, 331: 8, 373: 8, 379: 2, 382: 8, 384: 2, 385: 2, 397: 8, 415: 8, 439: 8, 441: 8, 449: 4, 461: 8, 463: 8, 472: 8, 512: 1, 513: 8, 514: 4, 515: 8, 516: 8, 517: 8, 518: 8, 519: 8, 520: 8, 581: 8, 583: 8, 585: 8, 643: 8, 645: 8, 674: 8, 747: 8, 750: 8, 752: 8, 753: 8, 755: 8, 757: 8, 758: 8, 759: 6, 760: 3, 766: 8, 767: 8, 770: 8, 773: 4, 774: 8, 778: 8, 781: 8, 782: 8, 783: 8, 793: 1, 815: 8, 822: 8, 828: 8, 829: 4, 841: 8, 846: 8, 847: 8, 851: 8, 855: 8, 865: 8, 881: 8, 883: 8, 885: 8, 887: 8, 888: 8, 890: 7, 892: 8, 893: 8, 894: 8, 902: 2, 909: 8, 925: 8, 927: 8, 928: 2, 931: 3, 934: 2, 936: 2, 939: 8, 943: 8, 949: 2, 965: 8, 980: 8, 985: 7, 993: 8, 997: 8, 999: 8, 1009: 8, 1010: 8, 1024: 8, 1025: 8, 1026: 8, 1028: 8, 1030: 8, 1031: 8, 1032: 8, 1033: 8, 1047: 8, 1048: 8, 1065: 8, 1073: 8
  },
  # Crosstrek 2018 (same platform as Subaru)
  ],
}

STEER_THRESHOLD = {
  CAR.IMPREZA: 80,
}

class ECU:
  CAM = 0

ECU_FINGERPRINT = {
  ECU.CAM: [ 257, 69, 290, 356],   # steer torque cmd, driver controls / SUBARU STUFF
}

DBC = {
  CAR.IMPREZA: dbc_dict('mercedes_E350_2011_pre_final', None),
}
