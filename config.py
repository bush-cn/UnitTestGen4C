LANGUAGE_MODE = "cpp"

LOG_DIR = r"D:\Code\UnitTestGen\logs"
LLM_LOG_DIR = LOG_DIR + r"\llm_logs"

# REPO_PATH = r"D:\Code\UnitTestGen\test_repo"
# REPO_PATH = r"D:\Code\UnitTestGen\mahm3lib"
# REPO_PATH = r"D:\Code\UnitTestGen\fzy"
REPO_PATH = r"D:\Code\UnitTestGen\sxiv"
CUSTOMIZED_TESTCODE_PATH = [
    # r"test"
]  # relative path
# EXCEPTE_PATH = [
#     r"D:\Code\UnitTestGen\mahm3lib\src\unity"
# ]
EXCEPTE_PATH = [
    r"D:\Code\UnitTestGen\fzy\deps"
]
RESOLVED_METAINFO_PATH = "D:\\Code\\UnitTestGen\\data\\"
ALL_METAINFO_PATH = r"D:\Code\UnitTestGen\data\all_metainfo.json"

TESTCASE_METAINFO_PATH = RESOLVED_METAINFO_PATH + "testcase_metainfo.json"
# 新增
FUNCTION_METAINFO_PATH = RESOLVED_METAINFO_PATH + "function_metainfo.json"
UDT_METAINFO_PATH = RESOLVED_METAINFO_PATH + "udt_metainfo.json"
GLOBAL_VARIABLE_METAINFO_PATH = RESOLVED_METAINFO_PATH + "global_variable_metainfo.json"

FUNCTION_SIMILARITY_PATH = RESOLVED_METAINFO_PATH + "function_similarity.json"
TESTCASE_ANALYSIS_RESULT_PATH = RESOLVED_METAINFO_PATH + "testcase_analysis_result.json"
CONTEXT_ANALYSIS_RESULT_PATH = RESOLVED_METAINFO_PATH + "context_analysis_result.json"

GENERATION_RESULT_PATH = "D:\\Code\\UnitTestGen\\results\\"

REFERENCE_THRESHOLD = 0.8 # 当相似度大于该阈值时，提供参考给大模型
UNITTEST_FRAMEWORK = "Unity"
