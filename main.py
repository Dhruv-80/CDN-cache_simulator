class CDNCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.access_order = []

    def get(self, url):
        if url in self.cache:
            # Resource found in cache (cache hit)
            self.access_order.remove(url)
            self.access_order.insert(0, url)
            return True  # Indicate a cache hit
        else:
            # Resource not found in cache (cache miss)
            if len(self.cache) >= self.capacity:
                # Cache is full, evict the least recently used item (LRU)
                removed_url = self.access_order.pop()
                del self.cache[removed_url]
            self.cache[url] = True
            self.access_order.insert(0, url)
            return False  # Indicate a cache miss

def main():
    print("CDN Cache Simulator")
    print("This program simulates a Content Delivery Network (CDN) cache using the Least Recently Used (LRU) eviction policy.")
    
    # Set the cache capacity to 10
    cache_capacity = 10
    print(f"Cache capacity is set to {cache_capacity} resources.")
    
    cdn_cache = CDNCache(cache_capacity)

    # Preload 10 resources into the cache
    preloaded_resources = [f"r{i}" for i in range(1, 11)]
    for resource in preloaded_resources:
        cdn_cache.get(resource)

    # Initialize the list of resources
    resource_list = preloaded_resources.copy()

    # Initialize hit and miss counters
    hit_count = 0
    miss_count = 0

    while True:
        user_request = input("Enter a resource request (or 'exit' to quit): ").strip()

        if user_request.lower() == "exit":
            break

        # Check if the user's request is in the cache
        is_cache_hit = cdn_cache.get(user_request)

        if is_cache_hit:
            hit_count += 1
        else:
            miss_count += 1

        # Update the resource list based on the user's request
        resource_list.insert(0, user_request)
        if len(resource_list) > cache_capacity:
            resource_list.pop()

    # Generate the log with most used resources first
    resource_list.reverse()
    log = resource_list

    # Calculate the hit and miss ratio
    total_requests = hit_count + miss_count
    hit_ratio = hit_count / total_requests
    miss_ratio = miss_count / total_requests

    # Display the log and hit/miss ratio
    print("\nResource Request Log:")
    for i, resource in enumerate(log):
        print(f"{i + 1}. {resource}")

    print("\nHit/Miss Ratio:")
    print(f"Hit Ratio: {hit_ratio:.2%}")
    print(f"Miss Ratio: {miss_ratio:.2%}")

if __name__ == "__main__":
    main()
