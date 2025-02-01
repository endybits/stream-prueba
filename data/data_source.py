# Mock function to simulate data retrieval
import asyncio

data = [
    {
      "x_axis": [
        {
          "trade_month": [
            "2021-11",
            "2021-12",
            "2022-01",
            "2022-02",
            "2022-03",
            "2022-05",
            "2022-06",
            "2022-07",
            "2022-08",
            "2022-09",
            "2022-10",
            "2022-11",
            "2022-12",
            "2023-01",
            "2023-02",
            "2023-03",
            "2023-04",
            "2023-05",
            "2023-06",
            "2023-07",
            "2023-08",
            "2023-09",
            "2023-10",
            "2023-11",
            "2023-12",
            "2024-01",
            "2024-02"
          ]
        }
      ],
      "y_axis": [
        {
          "monthly_return": [
            -5236.26,
            -8777.18,
            -22792.93,
            -8108.32,
            -3720.15,
            -9651.3,
            -7877.79,
            -5683.24,
            -6985.49,
            -4347.61,
            -5124.21,
            -6230.42,
            -1317.08,
            -6767.5,
            -7159.57,
            -3860.54,
            -6107.86,
            -6211.61,
            -1453.22,
            -11752.98,
            -3531.29,
            -4096.46,
            -4931.2,
            -3757,
            -8104.32,
            -2477,
            -7615
          ]
        }
      ],
      "chart_key": "chart_6",
      "chart_title": "monthly return per broker - PropReports",
      "chart_type": "bar",
      "visualization_needed": True,
      "reasoning": "comparing monthly returns across different brokers over time is best represented visually to identify trends and differences",
      "x_axis_label": "Trade Month",
      "y_axis_label": "Monthly Return ($)"
    },
    {
      "x_axis": [
        {
          "trade_month": [
            "2022-05",
            "2022-06",
            "2022-07",
            "2022-08",
            "2022-09",
            "2022-10",
            "2022-11",
            "2023-02",
            "2023-05",
            "2023-08",
            "2023-09",
            "2023-10",
            "2023-11",
            "2023-12",
            "2024-01",
            "2024-02",
            "2024-03",
            "2024-04",
            "2024-05",
            "2024-06",
            "2024-07"
          ]
        }
      ],
      "y_axis": [
        {
          "monthly_return": [
            10071.73,
            11213.46,
            2072.75,
            20874.53,
            7180.14,
            -48551.75,
            810.78,
            -11083.68,
            13162.05,
            -9070.85,
            -3515.43,
            3786.16,
            8492.98,
            32412.27,
            5794.84,
            -241.47,
            933.97,
            -101.18,
            -52.15,
            -331.72,
            -52.15
          ]
        }
      ],
      "chart_key": "chart_8",
      "chart_title": "monthly return per broker - CenterPoint Securities",
      "chart_type": "bar",
      "visualization_needed": True,
      "reasoning": "comparing monthly returns across different brokers over time is best represented visually to identify trends and differences",
      "x_axis_label": "Trade Month",
      "y_axis_label": "Monthly Return ($)"
    },
    {
      "x_axis": [
        {
          "trade_month": [
            "2022-11",
            "2022-12",
            "2023-01",
            "2023-02",
            "2023-03",
            "2023-04",
            "2023-05",
            "2023-06",
            "2023-07",
            "2023-08",
            "2023-09",
            "2023-10",
            "2023-11",
            "2023-12",
            "2024-01",
            "2024-02",
            "2024-03",
            "2024-04",
            "2024-05",
            "2024-06",
            "2024-08",
            "2024-10",
            "2024-11",
            "2025-01"
          ]
        }
      ],
      "y_axis": [
        {
          "monthly_return": [
            39732.43,
            105922.74,
            191709.02,
            91444,
            47632.74,
            214615.95,
            225959.39,
            157868.74,
            130998,
            396288.05,
            347875.9,
            395581.76,
            -168084,
            580887.91,
            85571.85,
            -660398.57,
            -61260.19,
            -385422.78,
            9458.81,
            88,
            556,
            270,
            -3400,
            0
          ]
        }
      ],
      "chart_key": "chart_10",
      "chart_title": "monthly return per broker - Think or Swim",
      "chart_type": "bar",
      "visualization_needed": True,
      "reasoning": "comparing monthly returns across different brokers over time is best represented visually to identify trends and differences",
      "x_axis_label": "Trade Month",
      "y_axis_label": "Monthly Return ($)"
    },
    {
      "x_axis": [
        {
          "trade_month": [
            "2022-12",
            "2023-01",
            "2023-02",
            "2023-03",
            "2023-04",
            "2023-05",
            "2023-06",
            "2023-07",
            "2023-08",
            "2023-09",
            "2023-10",
            "2023-11",
            "2023-12",
            "2024-01",
            "2024-02"
          ]
        }
      ],
      "y_axis": [
        {
          "monthly_return": [
            13920,
            -56259.76,
            9337,
            -35958,
            -26583.43,
            -36958,
            -30136,
            -14464,
            -25320,
            -12500,
            -25480,
            144281,
            -16769,
            108840,
            -15940
          ]
        }
      ],
      "chart_key": "chart_12",
      "chart_title": "monthly return per broker - Tradovate",
      "chart_type": "bar",
      "visualization_needed": True,
      "reasoning": "comparing monthly returns across different brokers over time is best represented visually to identify trends and differences",
      "x_axis_label": "Trade Month",
      "y_axis_label": "Monthly Return ($)"
    },
    {
      "x_axis": [
        {
          "trade_month": [
            "2022-12",
            "2023-01",
            "2023-02"
          ]
        }
      ],
      "y_axis": [
        {
          "monthly_return": [
            -960,
            -12720,
            4960
          ]
        }
      ],
      "chart_key": "chart_14",
      "chart_title": "monthly return per broker - Tradier",
      "chart_type": "bar",
      "visualization_needed": True,
      "reasoning": "comparing monthly returns across different brokers over time is best represented visually to identify trends and differences",
      "x_axis_label": "Trade Month",
      "y_axis_label": "Monthly Return ($)"
    },
    {
      "x_axis": [
        {
          "trade_month": [
            "2023-01",
            "2023-03",
            "2023-04",
            "2023-05",
            "2023-06",
            "2023-07",
            "2023-08",
            "2023-09",
            "2023-10",
            "2024-07",
            "2024-08",
            "2024-11",
            "2024-12"
          ]
        }
      ],
      "y_axis": [
        {
          "monthly_return": [
            7777.6,
            7960,
            -29400,
            24920,
            54840,
            16200,
            280,
            4160,
            -4832,
            -20600,
            -60200,
            51,
            -10000
          ]
        }
      ],
      "chart_key": "chart_16",
      "chart_title": "monthly return per broker - Manual Entry",
      "chart_type": "bar",
      "visualization_needed": True,
      "reasoning": "comparing monthly returns across different brokers over time is best represented visually to identify trends and differences",
      "x_axis_label": "Trade Month",
      "y_axis_label": "Monthly Return ($)"
    },
    {
      "x_axis": [
        {
          "trade_month": [
            "2023-08",
            "2023-09",
            "2023-10",
            "2023-11",
            "2023-12",
            "2024-01",
            "2024-02"
          ]
        }
      ],
      "y_axis": [
        {
          "monthly_return": [
            24936,
            25440,
            52280,
            27688,
            59824,
            -1280,
            -36896
          ]
        }
      ],
      "chart_key": "chart_18",
      "chart_title": "monthly return per broker - Trade Hawk",
      "chart_type": "bar",
      "visualization_needed": True,
      "reasoning": "comparing monthly returns across different brokers over time is best represented visually to identify trends and differences",
      "x_axis_label": "Trade Month",
      "y_axis_label": "Monthly Return ($)"
    },
    {
      "x_axis": [
        {
          "trade_month": [
            "2023-09",
            "2023-10",
            "2023-11"
          ]
        }
      ],
      "y_axis": [
        {
          "monthly_return": [
            -52863.92,
            485695.76,
            12600
          ]
        }
      ],
      "chart_key": "chart_20",
      "chart_title": "monthly return per broker - TD Ameritrade",
      "chart_type": "bar",
      "visualization_needed": True,
      "reasoning": "comparing monthly returns across different brokers over time is best represented visually to identify trends and differences",
      "x_axis_label": "Trade Month",
      "y_axis_label": "Monthly Return ($)"
    },
    {
      "x_axis": [
        {
          "trade_month": [
            "2023-12"
          ]
        }
      ],
      "y_axis": [
        {
          "monthly_return": [
            -104.75
          ]
        }
      ],
      "chart_key": "chart_22",
      "chart_title": "monthly return per broker - Backtest",
      "chart_type": "bar",
      "visualization_needed": True,
      "reasoning": "comparing monthly returns across different brokers over time is best represented visually to identify trends and differences",
      "x_axis_label": "Trade Month",
      "y_axis_label": "Monthly Return ($)"
    },
    {
      "x_axis": [
        {
          "trade_month": [
            "2024-01"
          ]
        }
      ],
      "y_axis": [
        {
          "monthly_return": [
            85.7
          ]
        }
      ],
      "chart_key": "chart_24",
      "chart_title": "monthly return per broker - Tastytrade/Tastyworks",
      "chart_type": "bar",
      "visualization_needed": True,
      "reasoning": "comparing monthly returns across different brokers over time is best represented visually to identify trends and differences",
      "x_axis_label": "Trade Month",
      "y_axis_label": "Monthly Return ($)"
    },
    {
      "x_axis": [
        {
          "trade_month": [
            "2024-03",
            "2024-04",
            "2024-05",
            "2024-06",
            "2024-07"
          ]
        }
      ],
      "y_axis": [
        {
          "monthly_return": [
            -82.56,
            -854.24,
            -875.46,
            -22.25,
            362.49
          ]
        }
      ],
      "chart_key": "chart_26",
      "chart_title": "monthly return per broker - ByBit",
      "chart_type": "bar",
      "visualization_needed": True,
      "reasoning": "comparing monthly returns across different brokers over time is best represented visually to identify trends and differences",
      "x_axis_label": "Trade Month",
      "y_axis_label": "Monthly Return ($)"
    },
    {
      "x_axis": [
        {
          "trade_month": [
            "2024-05"
          ]
        }
      ],
      "y_axis": [
        {
          "monthly_return": [
            12220
          ]
        }
      ],
      "chart_key": "chart_28",
      "chart_title": "monthly return per broker - ATAS Trading",
      "chart_type": "bar",
      "visualization_needed": True,
      "reasoning": "comparing monthly returns across different brokers over time is best represented visually to identify trends and differences",
      "x_axis_label": "Trade Month",
      "y_axis_label": "Monthly Return ($)"
    },
    {
      "x_axis": [
        {
          "trade_month": [
            "2024-11",
            "2024-12"
          ]
        }
      ],
      "y_axis": [
        {
          "monthly_return": [
            157.6,
            100.78
          ]
        }
      ],
      "chart_key": "chart_30",
      "chart_title": "monthly return per broker - MetaTrader 4 (MT4)",
      "chart_type": "bar",
      "visualization_needed": True,
      "reasoning": "comparing monthly returns across different brokers over time is best represented visually to identify trends and differences",
      "x_axis_label": "Trade Month",
      "y_axis_label": "Monthly Return ($)"
    }
  ],

async def get_data(user_id, user_input: str):
    await asyncio.sleep(1)
    return {
        "user_input": user_input,
        "data": data
    }



async def get_performance_ai_answer(user_id, user_input: str, data):
		await asyncio.sleep(1)
		return """
<p>Here's a detailed look at your returns per broker on a monthly basis. The data reveals some interesting trends across different brokers over time. Let's break it down by broker:</p><p>First up, we have the returns for PropReports:</p><chart_6><p>The bar chart above illustrates the monthly returns for PropReports. You can see significant fluctuations, especially in late 2022.</p><p>Next, let's look at CenterPoint Securities:</p><chart_8><p>This chart shows the monthly returns for CenterPoint Securities. Notice the sharp increase in returns during mid-2023, which is quite striking.</p><p>Now, let's examine Think or Swim:</p><chart_10><p>The returns for Think or Swim show a remarkable peak in late 2023, followed by a substantial drop. This could indicate some volatility in your trading strategy with this broker.</p><p>Moving on to Tradovate:</p><chart_12><p>Tradovate's returns also display some volatility, particularly with a notable drop in early 2023.</p><p>Next, we have Tradier:</p><chart_14><p>The returns for Tradier show a downward trend, especially in early 2023, which might be worth investigating further.</p><p>Now, let's check the Manual Entry broker:</p><chart_16><p>This chart indicates some fluctuations, with a significant drop in returns in mid-2024.</p><p>Next, we have Trade Hawk:</p><chart_18><p>Trade Hawk shows a consistent increase in returns, particularly in late 2023, which is promising.</p><p>Now, let's look at TD Ameritrade:</p><chart_20><p>TD Ameritrade's returns show a significant spike in October 2023, followed by a drop. This could be an area to explore further.</p><p>Lastly, we have Backtest:</p><chart_22><p>The returns for Backtest are relatively stable but show a slight decline in late 2023.</p><p>For Tastytrade/Tastyworks:</p><chart_24><p>The returns here are modest but positive, indicating a stable performance.</p><p>Next, ByBit:</p><chart_26><p>ByBit shows some fluctuations, particularly with a drop in early 2024.</p><p>Lastly, ATAS Trading:</p><chart_28><p>ATAS Trading shows a positive return in May 2024, which is encouraging.</p><p>Finally, let's look at MetaTrader 4 (MT4):</p><chart_30><p>The returns for MT4 show a slight increase towards the end of 2024, indicating a potential recovery.</p></p><p>Overall, the data suggests varying performance across brokers, with some showing significant volatility while others maintain a more stable return. Here are a few areas you might want to explore further:</p><ol>    <li>Investigate the reasons behind the sharp declines in returns for brokers like PropReports and Tradier.</li>    <li>Look into the strategies used during the months with peak returns, especially for CenterPoint Securities and Think or Swim.</li>    <li>Consider the impact of market conditions on your trading performance across different brokers.</li></ol><p>Would you like to dive deeper into any of these points?</p>
"""

