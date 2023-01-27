TransactionTypesList: list[str] = ['CashDeposit', 'Withdrawal', 'TravellerCheckEncash',
                                   'WithdrawalAndClose', 'WireTransferReceive', 'WireTransferSend', 'ATM',
                                   'MoneyTransferReceive', 'MoneyTransferSend', 'BuyCurrency',
                                   'SellCurrency', 'CurrencyExchange', 'CurrencyConversion', 'BanknoteExchange',
                                   'TravellerCheckBuy', 'BankCheckEncash', 'AccountOpening', 'CardCreation',
                                   'CapitalDeposit',
                                   'SecuritiesTransaction', 'FundsToAttract', 'CashBack', 'LoanBack', 'ReceiveDeposit',
                                   'ProfitCashIssue', 'ProfitMaterialIssue', 'LoanRepayment',
                                   'ParticipatingFeePayment', 'InsurancePremiumReceive', 'PensionContributionReceive',
                                   'InsuranceLossCompensation',
                                   'InsuranceLossPartialCompensation', 'PensionIssue', 'LifeInsuranceAmountIssue',
                                   'LifeInsuranceAmountPartialIssue',
                                   'ReinsurancePayment', 'LossCompensationByReinsurer', 'InsuranceMediatorFeePayment',
                                   'BorderCrossing', 'EMoneyReceive',
                                   'EMoneySend', 'FundsReceive', 'FundsSend', 'LoanDisburse', 'LoanBorrowing', 'OTHER']


NbgTransactionTypesList: list[str] = ['CurrencyWithCash', 'CashDeposit', 'ATMCashIn', 'BankCheckEncash', 'AbroadEBank',
                                      'AbroadNoAccount', 'AbroadATM', 'AbroadOther', 'AbroadReceive',
                                      'AbroadInstantSend',
                                      'AbroadInstantReceive', 'LoanWithSecurity', 'LoanWithDeposit', 'LoanWithForm',
                                      'LoanWithGemAndArt',
                                      'InternationalGuaranties', 'Esqro',
                                      'NominalAccount', 'PrepayCard', 'ATMLocalTransfer',
                                      'NoIdentification', 'HighRiskOther']

LegalFormTypesList: list[str] = ['LLC', 'JSC', 'GP', 'COOP', 'LP', 'TreasuryOrganization', 'PublicLegalEntity',
                                 'Community', 'Fund', 'Union',
                                 'PoliticalOrganization', 'ReligiousOrganization',
                                 'InternationalOrganization', 'ForeignEnterprise', 'ForeignNonProfitLegalEntity',
                                 'Diplomatic',
                                 'NonProfitLegalEntity', 'Other']
AccountTypesList: list[str] = ['Current', 'Correspondent', 'Deposit',
                               'Target', 'Loan', 'Card', 'Cash', 'Transit', 'transit_transfer', 'transit_other']

ActivityAreaTypesList: list[str] = ['ProfessionalProvider', 'Lottery', 'GemAndArt', 'Military', 'Chemicals', 'Nuclear',
                                    'DrugsNoResident',
                                    'NoneProfit', 'SportClub', 'InvestmentFund', 'Software', 'Holding', 'Assets',
                                    'TrustAgent',
                                    'RegisteredByTrustAgent', 'RealEstateAgency', 'ECurrencyExchange', 'Loan',
                                    'FarmaComp', 'BuildComp', 'ProfComp']
