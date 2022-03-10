"use strict";
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (Object.hasOwnProperty.call(mod, k)) result[k] = mod[k];
    result["default"] = mod;
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
const core = __importStar(require("@actions/core"));
class TaskParameters {
    constructor() {
        this._azureDevopsProjectUrl = "[AZ_DEVOPS_PROJECT_URL]";
        this._azurePipelineName = "[AZ_DEVOPS_PIPELINE_NAME]";
        this._azureDevopsToken = "[AZURE_DEVOPS_TOKEN]"; // '${{ secrets.AZURE_DEVOPS_TOKEN }}';
        this._azurePipelineVariables = '{[PIPELINE_INPUT_VARIABLES]}';
    }
    static getTaskParams() {
        if (!this.taskparams) {
            this.taskparams = new TaskParameters();
        }
        return this.taskparams;
    }
    get azureDevopsProjectUrl() {
        return this._azureDevopsProjectUrl;
    }
    get azurePipelineName() {
        return this._azurePipelineName;
    }
    get azureDevopsToken() {
        return this._azureDevopsToken;
    }
    get azurePipelineVariables() {
        return this._azurePipelineVariables;
    }
}
exports.TaskParameters = TaskParameters;
