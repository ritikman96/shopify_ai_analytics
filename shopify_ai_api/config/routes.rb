Rails.application.routes.draw do
    namespace :api do
        namespace:v1 do
            resource: question, only: [:create]
        end
    end
end