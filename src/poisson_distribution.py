import math

def poisson_distribution(event_freq, time_interval_1, predict_event_freq, time_interval_2):
    """
    Determines the probability of an
    event occurring over a specified
    period of time.
    """
    if time_interval_1 == time_interval_2:
        return (((event_freq ** predict_event_freq * math.e ** -event_freq) / math.factorial(predict_event_freq))) * 100
    else:
        factor = time_interval_2 / time_interval_1
        mean = event_freq * factor
        return (((mean ** predict_event_freq * math.e ** -mean) / math.factorial(predict_event_freq))) * 100




