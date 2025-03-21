# -*- coding: utf-8 -*-
# 版权所有 2019 深圳米筐科技有限公司（下称“米筐科技”）
#
# 除非遵守当前许可，否则不得使用本软件。
#
#     * 非商业用途（非商业用途指个人出于非商业目的使用本软件，或者高校、研究所等非营利机构出于教育、科研等目的使用本软件）：
#         遵守 Apache License 2.0（下称“Apache 2.0 许可”），
#         您可以在以下位置获得 Apache 2.0 许可的副本：http://www.apache.org/licenses/LICENSE-2.0。
#         除非法律有要求或以书面形式达成协议，否则本软件分发时需保持当前许可“原样”不变，且不得附加任何条件。
#
#     * 商业用途（商业用途指个人出于任何商业目的使用本软件，或者法人或其他组织出于任何目的使用本软件）：
#         未经米筐科技授权，任何个人不得出于任何商业目的使用本软件（包括但不限于向第三方提供、销售、出租、出借、转让本软件、
#         本软件的衍生产品、引用或借鉴了本软件功能或源代码的产品或服务），任何法人或其他组织不得出于任何目的使用本软件，
#         否则米筐科技有权追究相应的知识产权侵权责任。
#         在此前提下，对本软件的使用同样需要遵守 Apache 2.0 许可，Apache 2.0 许可与本许可冲突之处，以本许可为准。
#         详细的授权流程，请联系 public@ricequant.com 获取。
from pandas import Timestamp

from rqalpha.cmds import cli

config = {
    'base__accounts': (('stock', '1000000'),),
    'base__data_bundle_path': None,
    'base__end_date': Timestamp('2016-01-01 00:00:00'),
    'base__frequency': None,
    'base__init_positions': None,
    'base__margin_multiplier': None,
    'base__resume_mode': False,
    'base__round_price': False,
    'base__rqdatac_uri': None,
    'base__run_type': 'b',
    'base__source_code': None,
    'base__start_date': Timestamp('2014-01-01 00:00:00'),
    'base__strategy_file': r'.\examples\rsi.py',
    'config_path': None,
    'extra__context_vars': None,
    'extra__enable_profiler': None,
    'extra__locale': None,
    'extra__log_level': None,
    'extra__logger': (),
    'mod__sys_accounts__cash_return_by_stock_delisted': True,
    'mod__sys_accounts__dividend_reinvestment': None,
    'mod__sys_accounts__futures_settlement_price_type': None,
    'mod__sys_accounts__stock_t1': None,
    'mod__sys_accounts__validate_stock_position': True,
    'mod__sys_analyser__benchmark': None,
    'mod__sys_analyser__output_file': 'result.pkl',
    'mod__sys_analyser__plot': 'default',
    'mod__sys_analyser__plot_config__open_close_points': None,
    'mod__sys_analyser__plot_config__weekly_indicators': None,
    'mod__sys_analyser__plot_save_file': None,
    'mod__sys_analyser__report_save_path': None,
    'mod__sys_progress__show': True,
    'mod__sys_risk__validate_cash': True,
    'mod__sys_simulation__inactive_limit': None,
    'mod__sys_simulation__management_fee': (),
    'mod__sys_simulation__matching_type': None,
    'mod__sys_simulation__signal': None,
    'mod__sys_simulation__slippage': None,
    'mod__sys_simulation__slippage_model': None,
    'mod__sys_transaction_cost__cn_stock_min_commission': None,
    'mod__sys_transaction_cost__commission_multiplier': None,
    'mod__sys_transaction_cost__futures_commission_multiplier': None,
    'mod__sys_transaction_cost__pit_tax': False,
    'mod__sys_transaction_cost__stock_commission_multiplier': None,
    'mod__sys_transaction_cost__tax_multiplier': None
}


def entry_point():
    from rqalpha.mod.utils import inject_mod_commands
    inject_mod_commands()
    cli(obj={})


def entry(kwargs:dict):
    from rqalpha.mod.utils import inject_mod_commands
    from rqalpha.utils.config import parse_config
    from rqalpha import main
    import os

    inject_mod_commands()

    config_path = kwargs.get('config_path', None)
    if config_path is not None:
        config_path = os.path.abspath(config_path)
        kwargs.pop('config_path')
    if not kwargs.get('base__securities', None):
        kwargs.pop('base__securities', None)

    source_code = kwargs.get("base__source_code")
    cfg = parse_config(kwargs, config_path=config_path, click_type=True, source_code=source_code)
    source_code = cfg.base.source_code
    main.run(cfg, source_code=source_code)


if __name__ == '__main__':
    # entry_point()
    entry(config)
