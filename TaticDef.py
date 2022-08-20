import math
# Biblioteca para gerar os gráficos.
from tkinter import*
from tkinter.ttk import Combobox

# Valores passados.
tempo = [0.0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34, 0.36, 0.38, 0.40, 0.42, 0.44, 0.46, 0.48, 0.50, 0.52, 0.54, 0.56, 0.58, 0.60, 0.62, 0.64, 0.66, 0.68, 0.70, 0.72, 0.74, 0.76, 0.78, 0.80, 0.82, 0.84, 0.86, 0.88, 0.90, 0.92,	0.94,	0.96,	0.98,	1.00,	1.02,	1.04,	1.06,	1.08,	1.10,	1.12,	1.14,	1.16,	1.18,	1.20,	1.22,	1.24,	1.26,1.28,	1.30,	1.32,	1.34,	1.36,	1.38,	1.40,	1.42,	1.44, 1.46,	1.48,	1.50,	1.52,	1.54,	1.56,	1.58,	1.60,	1.62,	1.64,	1.66,	1.68,	1.70,	1.72,	1.74,	1.76,	1.78,	1.80,	1.82,	1.84,	1.86,	1.88,	1.90,	1.92,	1.94,	1.96,	1.98,	2.00,	2.02,	2.04,	2.06,	2.08,	2.10,	2.12,	2.14,	2.16,	2.18, 2.20,	2.22, 2.24,	2.26,	2.28,	2.30,	2.32,	2.34,	2.36,	2.38,	2.40,	2.42,	2.44,	2.46,	2.48,	2.50,	2.52,	2.54,	2.56,	2.58,	2.60,	2.62,	2.64,	2.66,	2.68, 2.70,	2.72,	2.74,	2.76,	2.78,	2.80,	2.82,	2.84,	2.86,	2.88,	2.90,	2.92,	2.94,	2.96,	2.98,	3.00,	3.02,	3.04,	3.06,	3.08,	3.10,	3.12,	3.14,	3.16,	3.18,	3.20,	3.22,	3.24,	3.26,	3.28,	3.30,	3.32,	3.34,	3.36,	3.38,	3.40,	3.42,	3.44, 3.46,	3.48,	3.50,	3.52,	3.54,	3.56,	3.58,	3.60,	3.62,	3.64,	3.66,	3.68,	3.70,	3.72,	3.74,	3.76,	3.78,	3.80,	3.82,	3.84,	3.86,	3.88,	3.90,	3.92,	3.94,	3.96,	3.98,	4.00,	4.02,	4.04,	4.06,	4.08,	4.10,	4.12,	4.14,	4.16,	4.18,	4.20,	4.22,	4.24, 4.26,	4.28,	4.30,	4.32,	4.34,	4.36,	4.38,	4.40,	4.42, 4.44,	4.46,	4.48,	4.50,	4.52,	4.54,	4.56,	4.58,	4.60,	4.62,	4.64,	4.66,	4.68,	4.70,	4.72,	4.74,	4.76,	4.78,	4.80,	4.82,	4.84,	4.86, 4.88,	4.90,	4.92,	4.94,	4.96,	4.98,	5.00,	5.02,	5.04,	5.06,	5.08,	5.10,	5.12, 5.14,	5.16,	5.18,	5.20,	5.22,	5.24,	5.26,	5.28,	5.30, 5.32,	5.34,	5.36,	5.38,	5.40,	5.42,	5.44,	5.46,	5.48,	5.50,	5.52,	5.54,	5.56,	5.58,	5.60,	5.62,	5.64,	5.66, 5.68,	5.70,	5.72,	5.74,	5.76,	5.78,	5.80,	5.82,	5.84,	5.86,	5.88,	5.90,	5.92,	5.94,	5.96,	5.98,	6.00,	6.02,	6.04,	6.06,	6.08,	6.10,	6.12,	6.14,	6.16,	6.18,	6.20,	6.22,	6.24,	6.26,	6.28,	6.30,	6.32,	6.34,	6.36,	6.38,	6.40,	6.42,	6.44,	6.46,	6.48,	6.50,	6.52,	6.54,	6.56,	6.58,	6.60,	6.62,	6.64,	6.66, 6.68,	6.70,	6.72,6.74,	6.76,	6.78,	6.80,	6.82,	6.84,	6.86,	6.88,	6.90,	6.92,	6.94,	6.96,	6.98,	7.00,	7.02,	7.04,	7.06,	7.08,	7.10,	7.12,	7.14,	7.16,	7.18,	7.20,	7.22,	7.24,	7.26,	7.28,	7.30,	7.32,	7.34,	7.36,	7.38,	7.40,	7.42,	7.44,	7.46,	7.48, 7.50,	7.52,	7.54,	7.56,	7.58,	7.60,	7.62,	7.64,	7.66,	7.68,	7.70,	7.72,	7.74,	7.76,	7.78,	7.80,	7.82,	7.84,	7.86,	7.88,	7.90,	7.92,	7.94,	7.96,	7.98,	8.00,	8.02,	8.04,	8.06,	8.08,	8.10,	8.12,	8.14,	8.16,	8.18,	8.20,	8.22,	8.24,	8.26,	8.28,	8.30,	8.32,	8.34,	8.36,	8.38,	8.40,	8.42,	8.44,	8.46,	8.48,	8.50,	8.52,	8.54,	8.56,	8.58,	8.60,	8.62,	8.64,	8.66,	8.68,	8.70,	8.72,	8.74, 8.76, 8.78,	8.80,	8.82,	8.84,	8.86,	8.88,	8.90,	8.92,	8.94,	8.96,	8.98,	9.00,	9.02,	9.04,	9.06,	9.08,	9.10,	9.12,	9.14,	9.16,	9.18,	9.20,	9.22,	9.24, 9.26,	9.28,	9.30,	9.32,	9.34, 9.36, 9.38]

bolaX = [1.00,	1.01,	1.02,	1.03,	1.04,	1.05,	1.06001,	1.07001,	1.08002, 1.09002,	1.10003, 1.11004,	1.12006	,1.13007,	1.4009,	1.15011,	1.16013,	1.17016,	1.18019,	1.19022,	1.20026,	1.2103,	1.22034,	1.23039,	1.24044,	1.2505,	1.26056,	1.27063,	1.2807,	1.29078,	1.30086,	1.31095,	1.32105,	1.33115,	1.34126, 1.35137,	1.36149,	1.37162,	1.38176,	1.3919,	1.40205, 1.41221,	1.42237,	1.43254,	1.44273,	1.45292,	1.46311,	1.47332,	1.48354,	1.49376,	1.504, 1.51424,	1.5245,	1.53476,	1.54504,	1.55532,	1.56562,	1.57593,	1.58624,	1.59657,	1.60691,	1.61726,	1.62763,	1.638,	1.64839,	1.65879,	1.6692,	1.67962,	1.69006,	1.70051,	1.71098,	1.72145,	1.73194,	1.74245,	1.75297,	1.7635,	1.77405,	1.78461,	1.79519,	1.80578,	1.81638,	1.82701,	1.83764, 1.8483,	1.85897,	1.86965, 1.88035,	1.89107,	1.90181,	1.91256,	1.92333,	1.93411,	1.94492,	1.95574, 1.96658,	1.97744,	1.98831,	1.99921,	2.01012,	2.02105,	2.032,	2.04297,	2.05396,	2.06497,	2.076,	2.08704,	2.09811,	2.1092,	2.12031,	2.13144,	2.14259,	2.15376,	2.16496,	2.17617,	2.18741,	2.19867,	2.20995,	2.22125,	2.23258,	2.24393,	2.2553,	2.26669,	2.27811,	2.28955,	2.30101,	2.3125,	2.32401,	2.33555,	2.34711,	2.35869,	2.3703,	2.38194,	2.3936,	2.40528,	2.417,	2.42873,	2.44049,	2.45228,	2.4641,	2.47594,	2.48781,	2.4997,	2.51163,	2.52357,	2.53555,	2.54756,	2.55959,	2.57165,	2.58374,	2.59585,	2.608,	2.62017,	2.63238,	2.64461,	2.65687,	2.66916,	2.68149,	2.69384,	2.70622,	2.71863,	2.73107,	2.74354,	2.75605,	2.76858,	2.78115,	2.79375,	2.80638,	2.81904,	2.83173,	2.84446,	2.85722,	2.87001,	2.88283,	2.89569,	2.90858,	2.9215,	2.93446,	2.94745,	2.96047,	2.97353,	2.98662,	2.99975,	3.01291,	3.02611,	3.03934,	3.05261,	3.06592,	3.07925,	3.09263,	3.10604,	3.11949,	3.13297,	3.14649,	3.16005,	3.17364,	3.18728,	3.20095,	3.21465,	3.2284,	3.24218,	3.256, 3,26986,	3.28376,	3.29769,	3.31167,	3.32568,	3.33974,	3.35383,	3.36797,	3.38214,	3.39635,	3.41061,	3.4249,	3.43924,	3.45361,	3.46803,	3.48249,	3.49699,	3.51153,	3.52611,	3.54074,	3.5554,	3.57011,	3.58487,	3.59966,	3.6145,	3.62938,	3.64431,	3.65928,	3.67429,	3.68934,	3.70444,	3.71959,	3.73478,	3.75001,	3.76529,	3.78062,	3.79599,	3.8114,	3.82686,	3.84237,	3.85792,	3.87352,	3.88917,	3.90486,	3.9206,	3.93638,	3.95222,	3.9681,	3.98402,	4.00,	4.01602,	4.0321,	4.04822,4.06439,	4.0806,	4.09687,	4.11319,	4.12955,	4.14597,	4.16243,	4.17895,	4.19551,	4.21213,	4.22879,	4.24551,	4.26228, 4.27909,	4.29596,	4.31288,	4.32986,	4.34688,	4.36396,	4.38109,	4.39827,	4.4155,	4.43279,	4.45013,	4.46752,	4.48496,	4.50246,	4.52002,	4.53762,	4.55529,	4.573, 4.59077,	4.6086,	4.62648,	4.64441,	4.6624,	4.68045,4.69855,	4.71671,	4.73492,	4.75319,	4.77152,	4.7899,	4.80834,	4.82683,	4.84539,	4.864,	4.88267,	4.9014,	4.92018,	4.93902,	4.95792,	4.97688,	4.9959,	5.01498,	5.03412,	5.05331,	5.07257,	5.09188,	5.11126,	5.13069,	5.15019,	5.16974, 5,18936,	5.20904,	5.22878,	5.24858,	5.26844,	5.28836,	5.30834,	5.32839,	5.3485,	5.36867,	5.38891,	5.4092,	5.42956,	5.44998,	5.47047,	5.49102,	5.51163,	5.53231,	5.55305,	5.57386,	5.59473,	5.61566,	5.63666,	5.65773,	5.67886,	5.70005,	5.72132,	5.74264,	5.76404,	5.7855,	5.80702,	5.82861,	5.85027,	5.872,	5.89379,	5.91565,	5.93758,	5.95958,	5.98164,	6.00378,	6.02598,	6.04825,	6.07058,	6.09299,	6.11547,	6.13801,	6.16063,	6.18331,	6.20607,	6.22889,	6.25179, 6.27475,	6.29779,	6.3209,	6.34407,	6.36732,	6.39064,	6.41404,	6.4375,	6.46104,	6.48464,	6.50832,	6.53208, 6.5559,	6.5798,	6.60377,	6.62782,	6.65194,	6.67613,	6.7004,	6.72474,	6.74915,	6.77364,	6.79821,	6.82285,	6.84756,	6.87235,	6.89722,	6.92216,	6.94717,	6.97226,	6.99743,	7.02268,	7.048,	7.0734,	7.09887,	7.12443,	7.15006,	7.17576,	7.20155,	7.22741,	7.25335,	7.27937,	7.30547,	7.33165,	7.3579,	7.38424,	7.41065,	7.43715,	7.46372,	7.49037,	7.51711,	7.54392,	7.57082,	7.59779,	7.62485,	7.65198,	7.6792,	7.7065,	7.73388, 7.76134,	7.78889,	7.81651,	7.84422,	7.87202,	7.89989,	7.92785,	7.95589,	7.98401,	8.01222,	8.04051,	8.06889,	8.09734,	8.12589,	8.15452,	8.18323,	8.21203,	8.24091,	8.26988,	8.29893,	8.32807,	8.35729,	8.3866,	8.416,	8.44548,	8.47505, 8.50471,	8.53445,	8.56428,	8.5942,	8.62421,	8.6543,	8.68448,	8.71475,	8.74511,	8.77556,	8.80609,	8.83672,	8.86743,	8.89823,	8.92912,	8.9601,	8.99117,	9.02234]

bolaY = [0.5,	0.51599, 0.53195,	0.54789,	0.56381,	0.5797,	0.59557,	0.61141,	0.62723,	0.64303,	0.6588,	0.67455,	0.69027,	0.70597,	0.72165,	0.7373,	0.75293,	0.76853,	0.78411,	0.79967,	0.8152,	0.83071,	0.84619,	0.86165,	0.87709,	0.8925,	0.90789,	0.92325,	0.93859,	0.95391,	0.9692,	0.98447,	0.99971,	1.01493, 1.03013,	1.0453,	1.06045,	1.07557	,1.09067, 1.10575,	1.1208,	1.13583,	1.15083,	1.16581,	1.18077,	1.1957,	1.21061,	1.22549,	1.24035,	1.25519,	1.27,	1.28479,	1.29955,	1.31429,	1.32901,	1.3437,	1.35837,	1.37301,	1.38763,	1.40223,	1.4168,	1.43135,	1.44587,	1.46037,	1.47485,	1.4893,	1.50373,	1.51813,	1.53251,	1.54687,	1.5612,	1.57551,	1.58979,	1.60405,	1.61829,	1.6325,	1.64669,	1.66085,	1.67499,	1.68911,	1.7032,	1.71727,	1.73131,	1.74533,	1.75933,	1.7733,	1.78725,	1.80117,	1.81507,	1.82895,	1.8428,	1.85663,	1.87043,	1.88421,	1.89797,	1.9117,	1.92541,	1.93909,	1.95275,	1.96639,	1.98,	1.99359,	2.00715,	2.02069,	2.03421,	2.0477,	2.06117,	2.07461,	2.08803, 2.10143,	2.1148,	2.12815,	2.14147,	2.15477,	2.16805, 2.1813,	2.19453, 2.20773,	2.22091,	2.23407,	2.2472,	2.26031,	2.27339,	2.28645,	2.29949,	2.3125,	2.32549,	2.33845,	2.35139,	2.36431,	2.3772,	2.39007,	2.40291,	2.41573,	2.42853,	2.4413,	2.45405,	2.46677,	2.47947,	2.49215,	2.5048,	2.51743,	2.53003,	2.54261,	2.55517,	2.5677,	2.58021,	2.59269,	2.60515,	2.61759,	2.63,	2.64239,	2.65475,	2.66709,	2.67941,	2.6917,	2.70397,	2.71621,	2.72843,	2.74063,	2.7528,	2.76495,	2.77707,	2.78917,	2.80125,	2.8133,	2.82533,	2.83733,	2.84931,	2.86127,	2.8732,	2.88511,	2.89699,	2.90885,	2.92069,	2.9325,	2.94429,	2.95605, 2.96779,	2.97951,	2.9912,	3.00287,	3.01451,	3.02613,	3.03773,	3.0493,	3.06085,	3.07237,	3.08387,	3.09535,	3.1068,	3.11823,	3.12963,	3.14101,	3.15237,	3.1637,	3.17501,	3.18629,	3.19755,	3.20879,	3.22, 3.23119,	3.24235,	3.25349,	3.26461,	3.2757,	3.28677,	3.29781,	3.30883,	3.31983,	3.3308,	3.34175,	3.35267,	3.36357,	3.37445,	3.3853,	3.39613,	3.40693,	3.41771,	3.42847,	3.4392,	3.44991,	3.46059, 3.47125,	3.48189,	3.4925,	3.50309,	3.51365,	3.52419,	3.53471,	3.5452, 3.55567,	3.56611,	3.57653,	3.58693,	3.5973,	3.60765,	3.61797,	3.62827,	3.63855,	3.6488,	3.65903,	3.66923,	3.67941,	3.68957,	3.6997,	3.70981,	3.71989,	3.72995,	3.73999,	3.75, 3.75999,	3.76995,	3.77989,	3.78981,	3.7997,	3.80957, 3.81941,	3.82923,	3.83903, 3.8488,	3.85855,	3.86827,	3.87797,	3.88765, 3.8973,	3.90693,	3.91653,	3.92611,	3.93567,	3.9452,	3.95471, 3.96419,	3.97365,	3.98309,	3.9925,	4.00189	,4.01125,	4.02059,	4.02991,	4.0392,	4.04847,	4.05771,	4.06693,	4.07613,	4.0853,	4.09445,	4.10357,	4.11267,	4.12175,	4.1308,	4.13983,	4.14883,	4.15781,	4.16677,	4.1757,	4.18461,	4.19349,	4.20235,	4.21119,	4.22,	4.22879,	4.23755,	4.24629,	4.25501,	4.2637,	4.27237,	4.28101,	4.28963,	4.29823,	4.3068,	4.31535,	4.32387, 4.33237,	4.34085,	4.3493,	4.35773,	4.36613,	4.37451,	4.38287,	4.3912,	4.39951,	4.40779,	4.41605,	4.42429,	4.4325,	4.44069,	4.44885,	4.45699,	4.46511,	4.4732,	4.48127,	4.48931,	4.49733,	4.50533,	4.5133,	4.52125,	4.52917,	4.53707,	4.54495,	4.5528,	4.56063,	4.56843,	4.57621,	4.58397,	4.5917,	4.59941,	4.60709,	4.61475,	4.62239,	4.63,	4.63759,	4.64515,	4.65269, 4.66021,	4.6677,	4.67517,	4.68261,	4.69003,	4.69743,	4.7048,	4.71215,	4.71947,	4.72677,	4.73405,	4.7413,	4.74853,	4.75573,	4.76291,	4.77007,	4.7772,	4.78431,	4.79139,	4.79845,	4.80549,	4.8125,	4.81949,	4.82645,	4.83339,	4.84031,	4.8472,	4.85407,	4.86091,	4.86773,	4.87453,	4.8813,	4.88805,	4.89477,	4.90147,	4.90815,	4.9148,	4.92143,	4.92803,	4.93461,	4.94117,	4.9477,	4.95421, 4.96069,	4.96715,	4.97359,	4.98,	4.98639,	4.99275,	4.99909,	5.00541,	5.0117,	5.01797,	5.02421,	5.03043,	5.03663,	5.0428,	5.04895,	5.05507,	5.06117,	5.06725,	5.0733,	5.07933,	5.08533,	5.09131,	5.09727,	5.1032,	5.10911,	5.11499,	5.12085,	5.12669, 5.1325,	5.13829,	5.14405,	5.14979,	5.15551,	5.1612,	5.16687, 5.17251,	5.17813,	5.18373,	5.1893,	5.19485,	5.20037,	5.20587,	5.21135,	5.2168,	5.22223,	5.22763,	5.23301,	5.23837,	5.2437,	5.24901,	5.25429,	5.25955,	5.26479,	5.27,	5.27519,	5.28035,	5.28549	,5.29061,	5.2957,	5.30077,5.30581,	5.31083,	5.31583,	5.3208,	5.32575,	5.33067,	5.33557,	5.34045,	5.3453,	5.35013,	5.35493,	5.35971,	5.36447]



tempoInterceptado  =  [ ] 
#robô
roboX  =  []
roboY  =  []
rVelocidadeX  =  [2] 
rVelocidadeY  =  [1] 
rAceleracaoX  =  [1] 
rAceleracaoY  =  [0.5] 
#bola
bolaInterceptadaX  =  [ ]
bolaInterceptadaY  =  [ ]
bVelInterceX  =  [ ]
bVelInterceY  =  [ ] 
bAcelIntercX  =  [ ] 
bAcelIntercY  =  [ ] 

cos  =  0 
sen  =  0
aceleracao  =  0.32  
raio  =  8.0
i = 0.0
float(i)

roboRx  =  [ ]
roboRy  =  [ ]
andamento = [0]

rx = 0
ry = 0
bolaBx = 0
bolaBy= 0
distRoboBolatotal = [0]
posroboX = 0
posroboY= 0

# variaveis para gerar gráficos.
groboRx = []
groboRy = []
gbolaBx = []
gbolaBy = []
gTempo = []
gdistancia = []
gveloRoboX = []
gveloRoboy = []
gacelacaoX = []
gacelacaoy = []
gacelacaoBolaX = []
gacelacaoBolay = []
gveloBolax = []
gveloBolay= []


aceleracaoBolax = []
aceleracaoBolay = []

velovidaddeBolax = []
velovidaddeBolay = []

velovidaddeBolax2 = []
velovidaddeBolay2 = []
# variaveis para interface gráfica.
dist1 = []
tempo1 = []
distTotal1 = []
posroboX1 = []
posroboy1 = []
posBolax = []
posBolay = []

# interface gráfica
janela = Tk()
janela.title('Tática de defesa')

rotulo = Label(janela, text='Dados sobre a interceptação', font=('Arial Bold', 12))
rotulo.place(relx = 0.5, rely = 0.05, anchor = CENTER)

Robox = Label(janela, text='Posição do robo em x: ', font =('Arial Bold', 12))
Robox.place(relx = 0.2, rely= 0.1, anchor = 'center')
#pegar os valores de X.
Robox2 = Entry(janela, width = 16, font=('Arial Bold', 12))
Robox2.place(relx = 0.5, rely = 0.1, anchor = CENTER)

Roboy = Label(janela, text='Posição do robo em y: ', font =('Arial Bold', 12))
Roboy.place(relx = 0.2, rely= 0.17, anchor = 'center')
#pegar os valores de Y.
Roboy2 = Entry(janela, width = 16, font=('Arial Bold', 12))
Roboy2.place(relx = 0.5, rely = 0.17, anchor = CENTER)

i = 0
j = 0
def andaRobo ():
        global j
        if(j == 0):
          #salvar as posições de X e Y.
          posroboX = float(Robox2.get()) 
          posroboY = float(Roboy2.get())

          roboX.insert(0, posroboX)
          roboY.insert(0, posroboY)
        tamBolax = len(bolaX)
        j = 1
        global i 
        while( i < tamBolax):
          #para achar a velocidade da bola, para isso usamos a função Velocidade escalar média, deltaS/deltaT.
          velovidaddeBolax.insert(i, (bolaX[i+1] - bolaX[i])/(tempo[i+1] - tempo[i]))
          velovidaddeBolay.insert(i, (bolaY[i+1] - bolaY[i])/(tempo[i+1] - tempo[i]))

          velovidaddeBolax2.insert(i, (bolaX[i+2] - bolaX[i+1])/(tempo[i+2] - tempo[i+1]))
          velovidaddeBolay2.insert(i, (bolaY[i+2] - bolaY[i+1])/(tempo[i+2] - tempo[i+1]))
          
          # achar a aceleração da bola usamos a função de Aceleração Média de um Móvel, deltaV/deltaT.
          aceleracaoBolax.insert(i, (velovidaddeBolax2[i] - velovidaddeBolax[i])/(tempo[i+1] - tempo[i]))
          aceleracaoBolay.insert(i, (velovidaddeBolay2[i] - velovidaddeBolay[i])/(tempo[i+1] - tempo[i]))

          #calcular a distancia do robo e da bola, usamos a função de distancia entre dois pontos.
          distRoboBolatotal.insert(i,(math.sqrt ( math.pow ( ( bolaX[i]-roboX[i]),2)+math.pow((bolaY[i]-roboY[i]),2))))
          if(distRoboBolatotal[i] == 0):
            print("a distancia do robô e da bola é igual a 0, ou seja, o robo ja está do lado da bola")
            break
          # calcular o seno e o cosseno.
          cos = (bolaX[i]-roboX[i])/distRoboBolatotal[i] 
          
          sen  =  ( bolaY[i]-roboY[i])/distRoboBolatotal[i] 

          if ( tempo[i] <= 2.0 ):
            #decompondo o vetor aceleração de X e Y. 
            rAceleracaoX.insert(i, aceleracao * cos )
            rAceleracaoY.insert(i, aceleracao * sen )
            
            # achando a velocidade até 2s com v = v + a * t. 
            rVelocidadeX.insert(i+1, rVelocidadeX [ i ]  +  ( rAceleracaoX [ i ] * tempo [ i ] ) )
            # utilizando função horária da posição em função do tempo pois o movimento eh uniformemente variado até 2s s = s0 + v0 + 0,5at²
            rVelocidadeY.insert(i+1, rVelocidadeY [ i ]  +  ( rAceleracaoY [ i ] * tempo [ i ] ) )
            roboX.insert(i+1, roboX [ i ]  +  ( rVelocidadeX[i]*tempo[i]) + (0.5 *(rAceleracaoX[i]*(tempo[i]*tempo[i]))))
            roboY.insert(i+1,roboY [ i ]  +  ( rVelocidadeY [ i ] * tempo [ i ] )  +  ( 0.5 * ( rAceleracaoY [ i ] * ( tempo [ i ] * tempo [ i ] ) ) ) )
          else:
            #depois que o robo atingir a velocidade máxima em 2s o movimento passa a ser uniforme	entao s = s0 + v * deltaT
            # decompondo a velocidade constante (2.0) em x e  (1.0) y
            rVelocidadeX[i]= 2.0 * cos
            rVelocidadeY[i] = 1.0 * sen 
            
            # usando na função horaria de deslocamento
            roboX.insert(i+1,roboX[i]+(rVelocidadeX[i]* 0.02)) 
            roboY.insert(i+1,roboY [ i ]  +  ( rVelocidadeY [ i ] * 0.02 ))

          #variáveis para gerar gráficos.
          gTempo.insert(i, tempo[i])
          groboRx.insert(i, roboX[i])
          groboRy.insert(i, roboY[i])  
          gbolaBx.insert(i, bolaX[i])       
          gbolaBy.insert(i, bolaY[i])
          gdistancia.insert(i, distRoboBolatotal[i])
          gveloRoboX.insert(i, rVelocidadeX[i])
          gveloRoboy.insert(i, rVelocidadeY[i])
          gacelacaoX.insert(i, rAceleracaoX[i])
          gacelacaoy.insert(i, rAceleracaoY[i])
          gacelacaoBolaX.insert(i,  aceleracaoBolax[i])
          gacelacaoBolay.insert(i,  aceleracaoBolay[i])
          gveloBolax.insert(i, velovidaddeBolax[i])
          gveloBolay.insert(i, velovidaddeBolay[i])

          i = i + 1
          # A distancia do robo está igual ao raio.
          if( distRoboBolatotal[i-1] >= raio):
            # Variáveis para interface gráfica.
            dist1.insert(0, distRoboBolatotal[0])
            tempo1.insert(0, tempo[i-1])
            distTotal1.insert(0, distRoboBolatotal[i-1])
            posroboX1.insert(0, abs(roboX[i-1])) 
            posroboy1.insert(0, abs(roboY[i-1]))
            posBolax.insert(0, bolaX[i-1])
            posBolay.insert(0,bolaY[i-1] )
            # apenas para segurança, Se a interface gráfica ocorrer algum problema.
            print("Distancia inicial da bola e do robo: ",distRoboBolatotal[0])
            print("Momento da intercptação, tempo =", tempo[i-1])
            print('distancia da bola no momento da interceptação: %.4f' % distRoboBolatotal[i-1])
            print('posição do robo em x no momento da interceptação: %.4f'% abs(roboX[i-1]))
            print('posição do bola em x: %.4f' % bolaX[i-1])
            print('posição da bola em y :%.4f'% bolaY[i-1])
            print('posição do robo em y no momento da interceptação: %.4f'% abs(roboY[i-1]))
            break

# Aplicar os resultados na interface gráfica.
result = Button(janela, text='verificar', command = andaRobo)
result.place(relx = 0.6, rely = 0.25, anchor = CENTER)

resposta = Label(janela, text='distancia inicial: ', font=('arial bold', 12))
resposta.place(relx = 0.18, rely= 0.3, anchor = 'center')

dist1 = Entry(janela, width = 25)
dist1.place(relx = 0.5, rely= 0.3, anchor = 'center')

resposta1 = Label(janela, text='tempo da interceptação: ', font=('arial bold', 12))
resposta1.place(relx = 0.21, rely= 0.35, anchor = 'center')

tempo1 = Entry(janela, width = 25)
tempo1.place(relx = 0.5, rely= 0.35, anchor = 'center')

resposta2 = Label(janela, text='distancia no momento da interceptação:', font=('arial bold', 12))
resposta2.place(relx = 0.28, rely= 0.4, anchor = 'center')

distTotal1 = Entry(janela, width = 25)
distTotal1.place(relx = 0.6, rely= 0.4, anchor = 'center')

resposta3 = Label(janela, text='posição do robo em x: ', font=('arial bold', 12))
resposta3.place(relx = 0.21, rely= 0.45, anchor = 'center')

posroboX1 = Entry(janela, width = 25)
posroboX1.place(relx = 0.5, rely= 0.45, anchor = 'center')

resposta4 = Label(janela, text='posição do robo em y: ', font=('arial bold', 12))
resposta4.place(relx = 0.21, rely= 0.50, anchor = 'center')

posroboy1 = Entry(janela, width = 25)
posroboy1.place(relx = 0.5, rely= 0.50, anchor = 'center')

resposta5 = Label(janela, text='posição da bola em x: ', font=('arial bold', 12))
resposta5.place(relx = 0.21, rely= 0.55, anchor = 'center')

posBolax = Entry(janela, width = 25)
posBolax.place(relx = 0.5, rely= 0.55, anchor = 'center')

resposta5 = Label(janela, text='posição da bola em y: ', font=('arial bold', 12))
resposta5.place(relx = 0.21, rely= 0.60, anchor = 'center')

posBolay = Entry(janela, width = 25)
posBolay.place(relx = 0.5, rely= 0.60, anchor = 'center')

janela.geometry('800x600')
janela.mainloop()

# Funções que geram os gráficos.
def geraGraficoBolay( bolaY, tempo):
  matplotlib.pyplot.title('trajetória bola Y')
  matplotlib.pyplot.xlabel('POSIÇÃO EM Y')
  matplotlib.pyplot.ylabel('TEMPO')

  matplotlib.pyplot.plot(bolaY, tempo)

  matplotlib.pyplot.show()


def geraGraficoDistancia(gTempo, gdistancia):
  #distancia do robo e da bola.
  matplotlib.pyplot.title('distancia do robo e da bola até o momento da interceptação')
  matplotlib.pyplot.xlabel('distancia')
  matplotlib.pyplot.ylabel('TEMPO')

  matplotlib.pyplot.plot(gdistancia, gTempo)

  matplotlib.pyplot.show()

def geraGraficoposicao(gbolaBx,gbolaBy,groboRx,groboRy):
  # esse grafico marca o instante da interceptação, sobre o tempo 
  matplotlib.pyplot.title('coordenadas do robo e da bola até o momento da interceptação')
  matplotlib.pyplot.xlabel('Azul = Posição do robo Laranja = Posição da bola')
  #posição em x.
  matplotlib.pyplot.plot(groboRx, groboRy)
  #posição em y.
  matplotlib.pyplot.plot(gbolaBx, gbolaBy)
  matplotlib.pyplot.show()

def geraGraficoposicaoTempo(gbolaBx,gbolaBy,groboRx,groboRy, gTempo):
  #distancia do robo e da bola.
  matplotlib.pyplot.title('trajetória do robo e da bola até o momento da interceptação \n em função do tempo')

  matplotlib.pyplot.xlabel('Azul = robo em x  Lar = robo em y  Verd = bola em x verm = bola em y')

#posição do robo
  matplotlib.pyplot.plot(groboRx, gTempo)
  matplotlib.pyplot.plot(groboRy, gTempo)
#posição da bola
  matplotlib.pyplot.plot(gbolaBx, gTempo)
  matplotlib.pyplot.plot(gbolaBy, gTempo)

  matplotlib.pyplot.show()


def geraGraficoVelo(gveloRoboX, gveloRoboy, gTempo):
  #velocidade do robo.
  matplotlib.pyplot.title('velocidade do robo até o momento da interceptação')
  matplotlib.pyplot.xlabel('Azul = velocidade do robo em x  Laranja = velocidade do robo em y ')


  matplotlib.pyplot.plot(gveloRoboX, gTempo)
  matplotlib.pyplot.plot(gveloRoboy, gTempo)
  matplotlib.pyplot.show()

def geraGraficoVeloBola(gveloBolax, gveloBolay, gTempo):
  #velocidade do robo.
  matplotlib.pyplot.title('velocidade da bola até o momento da interceptação')
  matplotlib.pyplot.xlabel('Azul = velocidade da bola em x  Laranja = velocidade da bola em y ')


  matplotlib.pyplot.plot(gveloBolax, gTempo)
  matplotlib.pyplot.plot(gveloBolay, gTempo)
  matplotlib.pyplot.show()

def geraGraficoAceleracaoRobo(gacelacaoX, gacelacaoy, gTempo):
  #aceleração.
  matplotlib.pyplot.title('aceleração do robo até o momento da interceptação')
  matplotlib.pyplot.xlabel('Azul = aceleração do robo em x  Laranja = aceleração do robo em y ')
  matplotlib.pyplot.plot(gacelacaoX, gTempo)
  matplotlib.pyplot.plot(gacelacaoy, gTempo)




  matplotlib.pyplot.show()

def geraGraficoAceleracaoBola(gacelacaoBolaX, gacelacaoBolay, gTempo):
  #aceleração.
  matplotlib.pyplot.title('aceleração da bola até o momento da interceptação')
  matplotlib.pyplot.xlabel('Azul = aceleração da bola em x  Laranja = aceleração da bola em y ')


  matplotlib.pyplot.plot(gacelacaoBolaX, gTempo)
  matplotlib.pyplot.plot(gacelacaoBolay, gTempo)

  matplotlib.pyplot.show()


geraGraficoVelo(gveloRoboX, gveloRoboy, gTempo)
geraGraficoVeloBola(gveloBolax, gveloBolay, gTempo)
geraGraficoposicaoTempo(gbolaBx,gbolaBy,groboRx,groboRy, gTempo)
geraGraficoposicao(gbolaBx,gbolaBy,groboRx,groboRy)
geraGraficoDistancia(gTempo, gdistancia)
geraGraficoAceleracaoRobo(gacelacaoX, gacelacaoy, gTempo)
geraGraficoAceleracaoBola(gacelacaoBolaX, gacelacaoBolay, gTempo)




