class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        # Build adjacency lists for the graph
        # directed_graph: for following method invocation chains
        # undirected_graph: for bidirectional connectivity check
        directed_graph = [[] for _ in range(n)]
        undirected_graph = [[] for _ in range(n)]
      
        for caller, callee in invocations:
            directed_graph[caller].append(callee)
            undirected_graph[caller].append(callee)
            undirected_graph[callee].append(caller)
      
        # Track which methods are suspicious (potentially buggy)
        is_suspicious = [False] * n
      
        def mark_suspicious_methods(method_id: int) -> None:
            """
            DFS to mark all methods reachable from the buggy method as suspicious.
            These are methods that could be affected by the bug.
            """
            is_suspicious[method_id] = True
            for next_method in directed_graph[method_id]:
                if not is_suspicious[next_method]:
                    mark_suspicious_methods(next_method)
      
        # Mark all methods reachable from the buggy method k
        mark_suspicious_methods(k)
      
        # Track visited methods in the second DFS
        visited = [False] * n
      
        def unmark_connected_suspicious(method_id: int) -> None:
            """
            DFS from non-suspicious methods to unmark suspicious methods
            that are connected to the non-suspicious part of the graph.
            This identifies suspicious methods that cannot be safely removed.
            """
            visited[method_id] = True
            for connected_method in undirected_graph[method_id]:
                if not visited[connected_method]:
                    is_suspicious[connected_method] = False
                    unmark_connected_suspicious(connected_method)
      
        # Check each non-suspicious method and unmark connected suspicious methods
        for method_id in range(n):
            if not is_suspicious[method_id] and not visited[method_id]:
                unmark_connected_suspicious(method_id)
      
        # Return all methods that are not suspicious (can remain in the system)
        return [method_id for method_id in range(n) if not is_suspicious[method_id]]