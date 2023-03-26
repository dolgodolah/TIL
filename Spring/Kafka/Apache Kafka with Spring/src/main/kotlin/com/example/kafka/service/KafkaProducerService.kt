package com.example.kafka.service

import com.example.kafka.dto.UserDTO
import com.fasterxml.jackson.databind.ObjectMapper
import org.springframework.kafka.core.KafkaTemplate
import org.springframework.stereotype.Service

@Service
class KafkaProducerService(
    private val kafkaTemplate: KafkaTemplate<String, String>
) {

    private val objectMapper = ObjectMapper()
    fun sendMessage(user: UserDTO) {
        val json = objectMapper.writeValueAsString(user)
        println("send message : $json")
        kafkaTemplate.send("example", json)
    }
}