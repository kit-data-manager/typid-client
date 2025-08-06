#  SPDX-FileCopyrightText: 2025 Karlsruhe Institute of Technology <maximilian.inckmann@kit.edu>
#  SPDX-License-Identifier: Apache-2.0
#
#  Copyright (c) 2025. Karlsruhe Institute of Technology
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  You may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import asyncio
import json
import logging
import os.path
from datetime import datetime
from typing import Any, Dict

import aiohttp

logger = logging.getLogger(__name__)
fh = logging.FileHandler(f"{__name__}.log")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

async def fetch_data(url: str) -> Dict[Any, Any]:
    """
    Fetches data from the specified URL.
    The data is cached in the CACHE_DIR.
    If the data is already cached, it is used instead of fetching fresh data.

    Args:
        url (str): The URL to fetch data from
        forceFresh (bool): Whether to force fetching fresh data. This tells the function to ignore cached data.

    Returns:
        dict: The fetched data

    Raises:
        ValueError: If the URL is invalid or the data cannot be fetched
    """
    if not url or url is None or not isinstance(url, str):
        raise ValueError("Invalid URL")

    filename = CACHE_DIR + "/" + url.replace("/", "_") + ".json"

    # check if data is cached
    if os.path.isfile(filename) and not forceFresh:
        with open(filename, "r") as f:  # load from cache
            result = json.load(f)  # get JSON
            if result is not None and isinstance(
                result, dict
            ):  # check if JSON is valid
                logger.info(f"Using cached data for {url}")
                return result  # return cached data

    try:
        logger.debug(f"Fetching {url}")
        async with aiohttp.ClientSession() as session:  # create a new session
            async with session.get(url) as response:  # fetch data
                if response.status == 200:  # check if the response is OK
                    with open(filename, "w") as c:  # save to cache
                        json.dump(await response.json(), c)
                    return await response.json()  # return fetched data
                else:  # if the response is not OK raise an error
                    logger.error(f"Failed to fetch {url}: {response.status}", response)
                    raise ValueError(
                        f"Failed to fetch {url}: {response.status}",
                        response,
                        datetime.now().isoformat(),
                    )
    except Exception as e:  # if an error occurs raise an error
        print(f"Error fetching {url}: {str(e)}")
        raise ValueError(str(e), url, datetime.now().isoformat())


async def fetch_multiple(urls: list[str]) -> list[Dict[Any, Any]]:
    """
    Fetches data from multiple URLs.
    This function is a wrapper around fetch_data that fetches data from multiple URLs concurrently.

    Args:
        urls (List[str]): A list of URLs to fetch data from
        forceFresh (bool): Whether to force fetching fresh data. This tells the function to ignore cached data.

    Returns:
        List[dict]: A list of fetched data

    Raises:
        ValueError: If the URLs are invalid or the data cannot be fetched
    """
    if not urls or urls is None or not isinstance(urls, list):
        raise ValueError("Invalid URLs. Please provide a list of URLs.")

    num_concurrent_requests = 100  # number of concurrent requests
    connector = aiohttp.TCPConnector(
        limit=num_concurrent_requests
    )  # create a new connector
    async with aiohttp.ClientSession(connector=connector):
        results = []
        for i in range(
            0, len(urls), num_concurrent_requests
        ):  # iterate over the URLs in batches
            batch = urls[i : i + num_concurrent_requests]  # get the current batch
            tasks = [
                asyncio.create_task(fetch_data(url, forceFresh)) for url in batch
            ]  # create tasks for each URL in the batch
            results.extend(
                await asyncio.gather(*tasks)
            )  # close the tasks and add the results to the list
        return results
