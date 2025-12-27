require "httparty"
 
class Api::V1::QuestionCOntroller < ApplicationController
    def create
        store_id = params[:store_id]
        question = params[:question]

        if store_id.blank || question.blank?
            return render json:{ error: 'Missing store_id or question'}, status: :bad_request
        end

        response = HTTParty.post(
        ENV['PYTHON_AI_URL']
        body: {store_id: store_id, question: question}. to_json,
        headers:{'Content-type'=> 'application/json'}
        )

        render json: response.parsed_response, status: response.code
    rescue => e
        render json: { error: e.message}, status:: internal_server_error
    end
end
