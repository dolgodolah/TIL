package com.example.kafka.conf

import org.apache.kafka.clients.admin.AdminClientConfig
import org.apache.kafka.clients.admin.NewTopic
import org.springframework.beans.factory.annotation.Value
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.kafka.core.KafkaAdmin
import java.util.HashMap

@Configuration
class KafkaTopicConfig(
    @Value("\${spring.kafka.bootstrap-servers}")
    private val bootstrapAddress: String
) {

    /*
    with the introduction of AdminClient in Kafka, we can now create topics programmatically.
    We need to add the KafkaAdmin Spring bean, which will automatically add topics for all beans of type NewTopic
     */
    @Bean
    fun kafkaAdmin(): KafkaAdmin {
        val config = HashMap<String, Any>().apply {
            this[AdminClientConfig.BOOTSTRAP_SERVERS_CONFIG] = bootstrapAddress
        }
        return KafkaAdmin(config)
    }

    @Bean
    fun topic1(): NewTopic {
        return NewTopic("example", 1, 1)
    }
}