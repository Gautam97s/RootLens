"use client";

import { useCallback, useEffect, useState } from "react";

import { fetchLogs } from "@/modules/logs/api";
import { LogsListResponse, LogsQueryParams } from "@/shared/types";

const DEFAULT_LIMIT = 10;

const defaultData: LogsListResponse = {
	total: 0,
	limit: DEFAULT_LIMIT,
	offset: 0,
	items: [],
};

export function useLogs(initialParams?: LogsQueryParams) {
	const [params, setParams] = useState<LogsQueryParams>({
		limit: DEFAULT_LIMIT,
		offset: 0,
		...initialParams,
	});
	const [data, setData] = useState<LogsListResponse>(defaultData);
	const [isLoading, setIsLoading] = useState<boolean>(true);
	const [error, setError] = useState<string | null>(null);

	const load = useCallback(async (nextParams: LogsQueryParams) => {
		setIsLoading(true);
		setError(null);
		try {
			const response = await fetchLogs(nextParams);
			setData(response);
		} catch {
			setError("Failed to load logs. Ensure backend is running.");
		} finally {
			setIsLoading(false);
		}
	}, []);

	useEffect(() => {
		load(params);
	}, [load, params]);

	const updateParams = useCallback((updates: Partial<LogsQueryParams>) => {
		setParams((prev) => ({ ...prev, ...updates }));
	}, []);

	return {
		data,
		params,
		isLoading,
		error,
		setParams: updateParams,
		refetch: () => load(params),
	};
}
