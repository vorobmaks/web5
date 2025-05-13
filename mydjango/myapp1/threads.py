from django.shortcuts import render
import requests
import concurrent.futures
import time
import plotly.express as px


def req(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("total_income", 0)
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return None


def parallel(url, num_requests, threads=5):
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        res = list(executor.map(req, [url] * num_requests))
    return res


def perf(url, number, threads):
    metrics = []
    for t in threads:
        start = time.time()
        parallel(url, number, threads=t)
        e = time.time() - start
        metrics.append({'threads': t, 'time': e})
    return metrics


def plot(metrics):
    fig = px.line(
        metrics,
        x='threads',
        y='time',
        color='requests',
        title='Performance',
        labels={"threads": "Number of Threads", "time": "Execution Time (s)", "requests": "Number of Requests"}
    )
    return fig.to_html()


def dash_thr(request):
    url = "http://127.0.0.1:8000/api/team/top-goals/"
    num = [10 ,50, 100]
    threads = range(2, 10, 2)

    all_metrics = []
    total_time = 0

    for num_requests in num:
        start = time.time()
        metrics = perf(url, num_requests, threads)
        all_metrics.extend([{'threads': m['threads'], 'time': m['time'], 'requests': num_requests} for m in metrics])
        total_time += time.time() - start

    plot_html = plot(all_metrics)

    return render(request, 'da.html', {'plot_html': plot_html, 'total_time': total_time})
