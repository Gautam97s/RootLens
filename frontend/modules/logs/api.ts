import apiClient from "@/shared/lib/api-client";
import { LogsListResponse, LogsQueryParams } from "@/shared/types";

export async function fetchLogs(params: LogsQueryParams): Promise<LogsListResponse> {
	const response = await apiClient.get<LogsListResponse>("/logs", { params });
	return response.data;
}
